# django-gssapi - SPNEGO/Kerberos authentication for Django applications
# Copyright (C) 2014-2019 Entr'ouvert
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging

import pytest


def test_ntlm(monkeypatch, client, caplog, db, settings, tmpdir):
    caplog.set_level(logging.DEBUG)
    import base64
    import os
    import gssapi
    try:
        import gssapi.mechs
    except ImportError:
        pytest.skip('no gssapi.mechs')
    import gssapi.raw as gb
    try:
        gssapi.mechs.Mechanism.from_int_seq(map(int, '1.3.6.1.4.1.311.2.2.10'.split('.')))
    except Exception as e:
        pytest.skip('NTLM mechanism is unavailable: %s' % e)

    ntlm_user_file = tmpdir / 'ntlm.txt'
    with ntlm_user_file.open('w') as fd:
        fd.write('DOMAIN:toto:tata\nCOIN:titi:tutu\nREVESTEL:tutu:tutu\n')
    settings.GSSAPI_NAME = gssapi.Name('http/testserver', gssapi.NameType.hostbased_service)
    monkeypatch.setitem(os.environ, 'NTLM_USER_FILE', str(ntlm_user_file))

    spnego_mech = gb.OID.from_int_seq("1.3.6.1.5.5.2")
    ntlm_mech = gb.OID.from_int_seq("1.3.6.1.4.1.311.2.2.10")
    service_name = gssapi.Name('http/testserver', gssapi.NameType.hostbased_service)

    username = gb.import_name(name=b"toto\\DOMAIN", name_type=gb.NameType.user)
    truc = gb.acquire_cred_with_password(
        name=username, password=b'tata', mechs=[ntlm_mech, spnego_mech])
    ntlm_client_creds = truc.creds
    ctx = gssapi.SecurityContext(usage='initiate', mech=spnego_mech, name=service_name, creds=ntlm_client_creds)
    client_token = ctx.step()

    response = client.get('/login/', HTTP_AUTHORIZATION='Negotiate %s' % base64.b64encode(client_token).decode('ascii'))
    assert response.status_code == 401
    assert '_auth_user_id' not in client.session
    assert response['WWW-Authenticate']
    tokens = response['WWW-Authenticate'].split()[1:]
    out_token = base64.b64decode(tokens[0])
    client_token = ctx.step(out_token)
    response = client.get(
        '/login/',
        HTTP_AUTHORIZATION='Negotiate %s' % base64.b64encode(client_token).decode('ascii'))
    assert response.status_code == 401
    assert '_auth_user_id' not in client.session
    assert response['WWW-Authenticate']
    # It's not a full NTLM as the server side never reach a completed state, it
    # seems that the server side state needs to be maintained between request
    # which is not feasible.
