# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

import binascii
import ipaddress
import os

import pytest

import six

from cryptography import x509
from cryptography.hazmat.backends.interfaces import RSABackend, X509Backend

from .test_x509 import _load_cert


class TestExtension(object):
    def test_not_an_oid(self):
        bc = x509.BasicConstraints(ca=False, path_length=None)
        with pytest.raises(TypeError):
            x509.Extension("notanoid", True, bc)

    def test_critical_not_a_bool(self):
        bc = x509.BasicConstraints(ca=False, path_length=None)
        with pytest.raises(TypeError):
            x509.Extension(x509.OID_BASIC_CONSTRAINTS, "notabool", bc)

    def test_repr(self):
        bc = x509.BasicConstraints(ca=False, path_length=None)
        ext = x509.Extension(x509.OID_BASIC_CONSTRAINTS, True, bc)
        assert repr(ext) == (
            "<Extension(oid=<ObjectIdentifier(oid=2.5.29.19, name=basicConst"
            "raints)>, critical=True, value=<BasicConstraints(ca=False, path"
            "_length=None)>)>"
        )


class TestNoticeReference(object):
    def test_notice_numbers_not_all_int(self):
        with pytest.raises(TypeError):
            x509.NoticeReference("org", [1, 2, "three"])

    def test_notice_numbers_none(self):
        with pytest.raises(TypeError):
            x509.NoticeReference("org", None)

    def test_repr(self):
        nr = x509.NoticeReference(u"org", [1, 3, 4])

        if six.PY3:
            assert repr(nr) == (
                "<NoticeReference(organization='org', notice_numbers=[1, 3, 4"
                "])>"
            )
        else:
            assert repr(nr) == (
                "<NoticeReference(organization=u'org', notice_numbers=[1, 3, "
                "4])>"
            )

    def test_eq(self):
        nr = x509.NoticeReference("org", [1, 2])
        nr2 = x509.NoticeReference("org", [1, 2])
        assert nr == nr2

    def test_ne(self):
        nr = x509.NoticeReference("org", [1, 2])
        nr2 = x509.NoticeReference("org", [1])
        nr3 = x509.NoticeReference(None, [1, 2])
        assert nr != nr2
        assert nr != nr3
        assert nr != object()


class TestUserNotice(object):
    def test_notice_reference_invalid(self):
        with pytest.raises(TypeError):
            x509.UserNotice("invalid", None)

    def test_notice_reference_none(self):
        un = x509.UserNotice(None, "text")
        assert un.notice_reference is None
        assert un.explicit_text == "text"

    def test_repr(self):
        un = x509.UserNotice(x509.NoticeReference(u"org", [1]), u"text")
        if six.PY3:
            assert repr(un) == (
                "<UserNotice(notice_reference=<NoticeReference(organization='"
                "org', notice_numbers=[1])>, explicit_text='text')>"
            )
        else:
            assert repr(un) == (
                "<UserNotice(notice_reference=<NoticeReference(organization=u"
                "'org', notice_numbers=[1])>, explicit_text=u'text')>"
            )

    def test_eq(self):
        nr = x509.NoticeReference("org", [1, 2])
        nr2 = x509.NoticeReference("org", [1, 2])
        un = x509.UserNotice(nr, "text")
        un2 = x509.UserNotice(nr2, "text")
        assert un == un2

    def test_ne(self):
        nr = x509.NoticeReference("org", [1, 2])
        nr2 = x509.NoticeReference("org", [1])
        un = x509.UserNotice(nr, "text")
        un2 = x509.UserNotice(nr2, "text")
        un3 = x509.UserNotice(nr, "text3")
        assert un != un2
        assert un != un3
        assert un != object()


class TestPolicyInformation(object):
    def test_invalid_policy_identifier(self):
        with pytest.raises(TypeError):
            x509.PolicyInformation("notanoid", None)

    def test_none_policy_qualifiers(self):
        pi = x509.PolicyInformation(x509.ObjectIdentifier("1.2.3"), None)
        assert pi.policy_identifier == x509.ObjectIdentifier("1.2.3")
        assert pi.policy_qualifiers is None

    def test_policy_qualifiers(self):
        pq = [u"string"]
        pi = x509.PolicyInformation(x509.ObjectIdentifier("1.2.3"), pq)
        assert pi.policy_identifier == x509.ObjectIdentifier("1.2.3")
        assert pi.policy_qualifiers == pq

    def test_invalid_policy_identifiers(self):
        with pytest.raises(TypeError):
            x509.PolicyInformation(x509.ObjectIdentifier("1.2.3"), [1, 2])

    def test_repr(self):
        pq = [u"string", x509.UserNotice(None, u"hi")]
        pi = x509.PolicyInformation(x509.ObjectIdentifier("1.2.3"), pq)
        if six.PY3:
            assert repr(pi) == (
                "<PolicyInformation(policy_identifier=<ObjectIdentifier(oid=1."
                "2.3, name=Unknown OID)>, policy_qualifiers=['string', <UserNo"
                "tice(notice_reference=None, explicit_text='hi')>])>"
            )
        else:
            assert repr(pi) == (
                "<PolicyInformation(policy_identifier=<ObjectIdentifier(oid=1."
                "2.3, name=Unknown OID)>, policy_qualifiers=[u'string', <UserN"
                "otice(notice_reference=None, explicit_text=u'hi')>])>"
            )

    def test_eq(self):
        pi = x509.PolicyInformation(
            x509.ObjectIdentifier("1.2.3"),
            [u"string", x509.UserNotice(None, u"hi")]
        )
        pi2 = x509.PolicyInformation(
            x509.ObjectIdentifier("1.2.3"),
            [u"string", x509.UserNotice(None, u"hi")]
        )
        assert pi == pi2

    def test_ne(self):
        pi = x509.PolicyInformation(
            x509.ObjectIdentifier("1.2.3"), [u"string"]
        )
        pi2 = x509.PolicyInformation(
            x509.ObjectIdentifier("1.2.3"), [u"string2"]
        )
        pi3 = x509.PolicyInformation(
            x509.ObjectIdentifier("1.2.3.4"), [u"string"]
        )
        assert pi != pi2
        assert pi != pi3
        assert pi != object()


class TestCertificatePolicies(object):
    def test_invalid_policies(self):
        pq = [u"string"]
        pi = x509.PolicyInformation(x509.ObjectIdentifier("1.2.3"), pq)
        with pytest.raises(TypeError):
            x509.CertificatePolicies([1, pi])

    def test_iter_len(self):
        pq = [u"string"]
        pi = x509.PolicyInformation(x509.ObjectIdentifier("1.2.3"), pq)
        cp = x509.CertificatePolicies([pi])
        assert len(cp) == 1
        for policyinfo in cp:
            assert policyinfo == pi

    def test_repr(self):
        pq = [u"string"]
        pi = x509.PolicyInformation(x509.ObjectIdentifier("1.2.3"), pq)
        cp = x509.CertificatePolicies([pi])
        if six.PY3:
            assert repr(cp) == (
                "<CertificatePolicies([<PolicyInformation(policy_identifier=<O"
                "bjectIdentifier(oid=1.2.3, name=Unknown OID)>, policy_qualifi"
                "ers=['string'])>])>"
            )
        else:
            assert repr(cp) == (
                "<CertificatePolicies([<PolicyInformation(policy_identifier=<O"
                "bjectIdentifier(oid=1.2.3, name=Unknown OID)>, policy_qualifi"
                "ers=[u'string'])>])>"
            )

    def test_eq(self):
        pi = x509.PolicyInformation(
            x509.ObjectIdentifier("1.2.3"), [u"string"]
        )
        cp = x509.CertificatePolicies([pi])
        pi2 = x509.PolicyInformation(
            x509.ObjectIdentifier("1.2.3"), [u"string"]
        )
        cp2 = x509.CertificatePolicies([pi2])
        assert cp == cp2

    def test_ne(self):
        pi = x509.PolicyInformation(
            x509.ObjectIdentifier("1.2.3"), [u"string"]
        )
        cp = x509.CertificatePolicies([pi])
        pi2 = x509.PolicyInformation(
            x509.ObjectIdentifier("1.2.3"), [u"string2"]
        )
        cp2 = x509.CertificatePolicies([pi2])
        assert cp != cp2
        assert cp != object()


@pytest.mark.requires_backend_interface(interface=RSABackend)
@pytest.mark.requires_backend_interface(interface=X509Backend)
class TestCertificatePoliciesExtension(object):
    def test_cps_uri_policy_qualifier(self, backend):
        cert = _load_cert(
            os.path.join("x509", "custom", "cp_cps_uri.pem"),
            x509.load_pem_x509_certificate,
            backend
        )

        cp = cert.extensions.get_extension_for_oid(
            x509.OID_CERTIFICATE_POLICIES
        ).value

        assert cp == x509.CertificatePolicies([
            x509.PolicyInformation(
                x509.ObjectIdentifier("2.16.840.1.12345.1.2.3.4.1"),
                [u"http://other.com/cps"]
            )
        ])

    def test_user_notice_with_notice_reference(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "cp_user_notice_with_notice_reference.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )

        cp = cert.extensions.get_extension_for_oid(
            x509.OID_CERTIFICATE_POLICIES
        ).value

        assert cp == x509.CertificatePolicies([
            x509.PolicyInformation(
                x509.ObjectIdentifier("2.16.840.1.12345.1.2.3.4.1"),
                [
                    u"http://example.com/cps",
                    u"http://other.com/cps",
                    x509.UserNotice(
                        x509.NoticeReference(u"my org", [1, 2, 3, 4]),
                        u"thing"
                    )
                ]
            )
        ])

    def test_user_notice_with_explicit_text(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "cp_user_notice_with_explicit_text.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )

        cp = cert.extensions.get_extension_for_oid(
            x509.OID_CERTIFICATE_POLICIES
        ).value

        assert cp == x509.CertificatePolicies([
            x509.PolicyInformation(
                x509.ObjectIdentifier("2.16.840.1.12345.1.2.3.4.1"),
                [x509.UserNotice(None, u"thing")]
            )
        ])

    def test_user_notice_no_explicit_text(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "cp_user_notice_no_explicit_text.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )

        cp = cert.extensions.get_extension_for_oid(
            x509.OID_CERTIFICATE_POLICIES
        ).value

        assert cp == x509.CertificatePolicies([
            x509.PolicyInformation(
                x509.ObjectIdentifier("2.16.840.1.12345.1.2.3.4.1"),
                [
                    x509.UserNotice(
                        x509.NoticeReference(u"my org", [1, 2, 3, 4]),
                        None
                    )
                ]
            )
        ])


class TestKeyUsage(object):
    def test_key_agreement_false_encipher_decipher_true(self):
        with pytest.raises(ValueError):
            x509.KeyUsage(
                digital_signature=False,
                content_commitment=False,
                key_encipherment=False,
                data_encipherment=False,
                key_agreement=False,
                key_cert_sign=False,
                crl_sign=False,
                encipher_only=True,
                decipher_only=False
            )

        with pytest.raises(ValueError):
            x509.KeyUsage(
                digital_signature=False,
                content_commitment=False,
                key_encipherment=False,
                data_encipherment=False,
                key_agreement=False,
                key_cert_sign=False,
                crl_sign=False,
                encipher_only=True,
                decipher_only=True
            )

        with pytest.raises(ValueError):
            x509.KeyUsage(
                digital_signature=False,
                content_commitment=False,
                key_encipherment=False,
                data_encipherment=False,
                key_agreement=False,
                key_cert_sign=False,
                crl_sign=False,
                encipher_only=False,
                decipher_only=True
            )

    def test_properties_key_agreement_true(self):
        ku = x509.KeyUsage(
            digital_signature=True,
            content_commitment=True,
            key_encipherment=False,
            data_encipherment=False,
            key_agreement=False,
            key_cert_sign=True,
            crl_sign=False,
            encipher_only=False,
            decipher_only=False
        )
        assert ku.digital_signature is True
        assert ku.content_commitment is True
        assert ku.key_encipherment is False
        assert ku.data_encipherment is False
        assert ku.key_agreement is False
        assert ku.key_cert_sign is True
        assert ku.crl_sign is False

    def test_key_agreement_true_properties(self):
        ku = x509.KeyUsage(
            digital_signature=False,
            content_commitment=False,
            key_encipherment=False,
            data_encipherment=False,
            key_agreement=True,
            key_cert_sign=False,
            crl_sign=False,
            encipher_only=False,
            decipher_only=True
        )
        assert ku.key_agreement is True
        assert ku.encipher_only is False
        assert ku.decipher_only is True

    def test_key_agreement_false_properties(self):
        ku = x509.KeyUsage(
            digital_signature=False,
            content_commitment=False,
            key_encipherment=False,
            data_encipherment=False,
            key_agreement=False,
            key_cert_sign=False,
            crl_sign=False,
            encipher_only=False,
            decipher_only=False
        )
        assert ku.key_agreement is False
        with pytest.raises(ValueError):
            ku.encipher_only

        with pytest.raises(ValueError):
            ku.decipher_only

    def test_repr_key_agreement_false(self):
        ku = x509.KeyUsage(
            digital_signature=True,
            content_commitment=True,
            key_encipherment=False,
            data_encipherment=False,
            key_agreement=False,
            key_cert_sign=True,
            crl_sign=False,
            encipher_only=False,
            decipher_only=False
        )
        assert repr(ku) == (
            "<KeyUsage(digital_signature=True, content_commitment=True, key_en"
            "cipherment=False, data_encipherment=False, key_agreement=False, k"
            "ey_cert_sign=True, crl_sign=False, encipher_only=None, decipher_o"
            "nly=None)>"
        )

    def test_repr_key_agreement_true(self):
        ku = x509.KeyUsage(
            digital_signature=True,
            content_commitment=True,
            key_encipherment=False,
            data_encipherment=False,
            key_agreement=True,
            key_cert_sign=True,
            crl_sign=False,
            encipher_only=False,
            decipher_only=False
        )
        assert repr(ku) == (
            "<KeyUsage(digital_signature=True, content_commitment=True, key_en"
            "cipherment=False, data_encipherment=False, key_agreement=True, k"
            "ey_cert_sign=True, crl_sign=False, encipher_only=False, decipher_"
            "only=False)>"
        )

    def test_eq(self):
        ku = x509.KeyUsage(
            digital_signature=False,
            content_commitment=False,
            key_encipherment=False,
            data_encipherment=False,
            key_agreement=True,
            key_cert_sign=False,
            crl_sign=False,
            encipher_only=False,
            decipher_only=True
        )
        ku2 = x509.KeyUsage(
            digital_signature=False,
            content_commitment=False,
            key_encipherment=False,
            data_encipherment=False,
            key_agreement=True,
            key_cert_sign=False,
            crl_sign=False,
            encipher_only=False,
            decipher_only=True
        )
        assert ku == ku2

    def test_ne(self):
        ku = x509.KeyUsage(
            digital_signature=False,
            content_commitment=False,
            key_encipherment=False,
            data_encipherment=False,
            key_agreement=True,
            key_cert_sign=False,
            crl_sign=False,
            encipher_only=False,
            decipher_only=True
        )
        ku2 = x509.KeyUsage(
            digital_signature=False,
            content_commitment=False,
            key_encipherment=False,
            data_encipherment=False,
            key_agreement=False,
            key_cert_sign=False,
            crl_sign=False,
            encipher_only=False,
            decipher_only=False
        )
        assert ku != ku2
        assert ku != object()


class TestSubjectKeyIdentifier(object):
    def test_properties(self):
        value = binascii.unhexlify(b"092384932230498bc980aa8098456f6ff7ff3ac9")
        ski = x509.SubjectKeyIdentifier(value)
        assert ski.digest == value

    def test_repr(self):
        ski = x509.SubjectKeyIdentifier(
            binascii.unhexlify(b"092384932230498bc980aa8098456f6ff7ff3ac9")
        )
        ext = x509.Extension(x509.OID_SUBJECT_KEY_IDENTIFIER, False, ski)
        if six.PY3:
            assert repr(ext) == (
                "<Extension(oid=<ObjectIdentifier(oid=2.5.29.14, name=subjectK"
                "eyIdentifier)>, critical=False, value=<SubjectKeyIdentifier(d"
                "igest=b\'\\t#\\x84\\x93\"0I\\x8b\\xc9\\x80\\xaa\\x80\\x98Eoo"
                "\\xf7\\xff:\\xc9\')>)>"
            )
        else:
            assert repr(ext) == (
                "<Extension(oid=<ObjectIdentifier(oid=2.5.29.14, name=subjectK"
                "eyIdentifier)>, critical=False, value=<SubjectKeyIdentifier(d"
                "igest=\'\\t#\\x84\\x93\"0I\\x8b\\xc9\\x80\\xaa\\x80\\x98Eoo"
                "\\xf7\\xff:\\xc9\')>)>"
            )

    def test_eq(self):
        ski = x509.SubjectKeyIdentifier(
            binascii.unhexlify(b"092384932230498bc980aa8098456f6ff7ff3ac9")
        )
        ski2 = x509.SubjectKeyIdentifier(
            binascii.unhexlify(b"092384932230498bc980aa8098456f6ff7ff3ac9")
        )
        assert ski == ski2

    def test_ne(self):
        ski = x509.SubjectKeyIdentifier(
            binascii.unhexlify(b"092384932230498bc980aa8098456f6ff7ff3ac9")
        )
        ski2 = x509.SubjectKeyIdentifier(
            binascii.unhexlify(b"aa8098456f6ff7ff3ac9092384932230498bc980")
        )
        assert ski != ski2
        assert ski != object()


class TestAuthorityKeyIdentifier(object):
    def test_authority_cert_issuer_not_generalname(self):
        with pytest.raises(TypeError):
            x509.AuthorityKeyIdentifier(b"identifier", ["notname"], 3)

    def test_authority_cert_serial_number_not_integer(self):
        dirname = x509.DirectoryName(
            x509.Name([
                x509.NameAttribute(x509.ObjectIdentifier('oid'), 'value1'),
                x509.NameAttribute(x509.ObjectIdentifier('oid2'), 'value2'),
            ])
        )
        with pytest.raises(TypeError):
            x509.AuthorityKeyIdentifier(b"identifier", [dirname], "notanint")

    def test_authority_issuer_none_serial_not_none(self):
        with pytest.raises(ValueError):
            x509.AuthorityKeyIdentifier(b"identifier", None, 3)

    def test_authority_issuer_not_none_serial_none(self):
        dirname = x509.DirectoryName(
            x509.Name([
                x509.NameAttribute(x509.ObjectIdentifier('oid'), 'value1'),
                x509.NameAttribute(x509.ObjectIdentifier('oid2'), 'value2'),
            ])
        )
        with pytest.raises(ValueError):
            x509.AuthorityKeyIdentifier(b"identifier", [dirname], None)

    def test_authority_cert_serial_and_issuer_none(self):
        aki = x509.AuthorityKeyIdentifier(b"id", None, None)
        assert aki.key_identifier == b"id"
        assert aki.authority_cert_issuer is None
        assert aki.authority_cert_serial_number is None

    def test_repr(self):
        dirname = x509.DirectoryName(
            x509.Name([x509.NameAttribute(x509.OID_COMMON_NAME, 'myCN')])
        )
        aki = x509.AuthorityKeyIdentifier(b"digest", [dirname], 1234)

        if six.PY3:
            assert repr(aki) == (
                "<AuthorityKeyIdentifier(key_identifier=b'digest', authority_"
                "cert_issuer=[<DirectoryName(value=<Name([<NameAttribute(oid="
                "<ObjectIdentifier(oid=2.5.4.3, name=commonName)>, value='myC"
                "N')>])>)>], authority_cert_serial_number=1234)>"
            )
        else:
            assert repr(aki) == (
                "<AuthorityKeyIdentifier(key_identifier='digest', authority_ce"
                "rt_issuer=[<DirectoryName(value=<Name([<NameAttribute(oid=<Ob"
                "jectIdentifier(oid=2.5.4.3, name=commonName)>, value='myCN')>"
                "])>)>], authority_cert_serial_number=1234)>"
            )

    def test_eq(self):
        dirname = x509.DirectoryName(
            x509.Name([x509.NameAttribute(x509.OID_COMMON_NAME, 'myCN')])
        )
        aki = x509.AuthorityKeyIdentifier(b"digest", [dirname], 1234)
        dirname2 = x509.DirectoryName(
            x509.Name([x509.NameAttribute(x509.OID_COMMON_NAME, 'myCN')])
        )
        aki2 = x509.AuthorityKeyIdentifier(b"digest", [dirname2], 1234)
        assert aki == aki2

    def test_ne(self):
        dirname = x509.DirectoryName(
            x509.Name([x509.NameAttribute(x509.OID_COMMON_NAME, 'myCN')])
        )
        dirname5 = x509.DirectoryName(
            x509.Name([x509.NameAttribute(x509.OID_COMMON_NAME, 'aCN')])
        )
        aki = x509.AuthorityKeyIdentifier(b"digest", [dirname], 1234)
        aki2 = x509.AuthorityKeyIdentifier(b"diges", [dirname], 1234)
        aki3 = x509.AuthorityKeyIdentifier(b"digest", None, None)
        aki4 = x509.AuthorityKeyIdentifier(b"digest", [dirname], 12345)
        aki5 = x509.AuthorityKeyIdentifier(b"digest", [dirname5], 12345)
        assert aki != aki2
        assert aki != aki3
        assert aki != aki4
        assert aki != aki5
        assert aki != object()


class TestBasicConstraints(object):
    def test_ca_not_boolean(self):
        with pytest.raises(TypeError):
            x509.BasicConstraints(ca="notbool", path_length=None)

    def test_path_length_not_ca(self):
        with pytest.raises(ValueError):
            x509.BasicConstraints(ca=False, path_length=0)

    def test_path_length_not_int(self):
        with pytest.raises(TypeError):
            x509.BasicConstraints(ca=True, path_length=1.1)

        with pytest.raises(TypeError):
            x509.BasicConstraints(ca=True, path_length="notint")

    def test_path_length_negative(self):
        with pytest.raises(TypeError):
            x509.BasicConstraints(ca=True, path_length=-1)

    def test_repr(self):
        na = x509.BasicConstraints(ca=True, path_length=None)
        assert repr(na) == (
            "<BasicConstraints(ca=True, path_length=None)>"
        )

    def test_eq(self):
        na = x509.BasicConstraints(ca=True, path_length=None)
        na2 = x509.BasicConstraints(ca=True, path_length=None)
        assert na == na2

    def test_ne(self):
        na = x509.BasicConstraints(ca=True, path_length=None)
        na2 = x509.BasicConstraints(ca=True, path_length=1)
        na3 = x509.BasicConstraints(ca=False, path_length=None)
        assert na != na2
        assert na != na3
        assert na != object()


class TestExtendedKeyUsage(object):
    def test_not_all_oids(self):
        with pytest.raises(TypeError):
            x509.ExtendedKeyUsage(["notoid"])

    def test_iter_len(self):
        eku = x509.ExtendedKeyUsage([
            x509.ObjectIdentifier("1.3.6.1.5.5.7.3.1"),
            x509.ObjectIdentifier("1.3.6.1.5.5.7.3.2"),
        ])
        assert len(eku) == 2
        assert list(eku) == [
            x509.OID_SERVER_AUTH,
            x509.OID_CLIENT_AUTH
        ]

    def test_repr(self):
        eku = x509.ExtendedKeyUsage([
            x509.ObjectIdentifier("1.3.6.1.5.5.7.3.1"),
            x509.ObjectIdentifier("1.3.6.1.5.5.7.3.2"),
        ])
        assert repr(eku) == (
            "<ExtendedKeyUsage([<ObjectIdentifier(oid=1.3.6.1.5.5.7.3.1, name="
            "serverAuth)>, <ObjectIdentifier(oid=1.3.6.1.5.5.7.3.2, name=clien"
            "tAuth)>])>"
        )

    def test_eq(self):
        eku = x509.ExtendedKeyUsage([
            x509.ObjectIdentifier("1.3.6"), x509.ObjectIdentifier("1.3.7")
        ])
        eku2 = x509.ExtendedKeyUsage([
            x509.ObjectIdentifier("1.3.6"), x509.ObjectIdentifier("1.3.7")
        ])
        assert eku == eku2

    def test_ne(self):
        eku = x509.ExtendedKeyUsage([x509.ObjectIdentifier("1.3.6")])
        eku2 = x509.ExtendedKeyUsage([x509.ObjectIdentifier("1.3.6.1")])
        assert eku != eku2
        assert eku != object()


@pytest.mark.requires_backend_interface(interface=RSABackend)
@pytest.mark.requires_backend_interface(interface=X509Backend)
class TestExtensions(object):
    def test_no_extensions(self, backend):
        cert = _load_cert(
            os.path.join("x509", "verisign_md2_root.pem"),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions
        assert len(ext) == 0
        assert list(ext) == []
        with pytest.raises(x509.ExtensionNotFound) as exc:
            ext.get_extension_for_oid(x509.OID_BASIC_CONSTRAINTS)

        assert exc.value.oid == x509.OID_BASIC_CONSTRAINTS

    def test_one_extension(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "basic_constraints_not_critical.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )
        extensions = cert.extensions
        ext = extensions.get_extension_for_oid(x509.OID_BASIC_CONSTRAINTS)
        assert ext is not None
        assert ext.value.ca is False

    def test_duplicate_extension(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "two_basic_constraints.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )
        with pytest.raises(x509.DuplicateExtension) as exc:
            cert.extensions

        assert exc.value.oid == x509.OID_BASIC_CONSTRAINTS

    def test_unsupported_critical_extension(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "unsupported_extension_critical.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )
        with pytest.raises(x509.UnsupportedExtension) as exc:
            cert.extensions

        assert exc.value.oid == x509.ObjectIdentifier("1.2.3.4")

    def test_unsupported_extension(self, backend):
        # TODO: this will raise an exception when all extensions are complete
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "unsupported_extension.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )
        extensions = cert.extensions
        assert len(extensions) == 0


@pytest.mark.requires_backend_interface(interface=RSABackend)
@pytest.mark.requires_backend_interface(interface=X509Backend)
class TestBasicConstraintsExtension(object):
    def test_ca_true_pathlen_6(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "PKITS_data", "certs", "pathLenConstraint6CACert.crt"
            ),
            x509.load_der_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_BASIC_CONSTRAINTS
        )
        assert ext is not None
        assert ext.critical is True
        assert ext.value.ca is True
        assert ext.value.path_length == 6

    def test_path_length_zero(self, backend):
        cert = _load_cert(
            os.path.join("x509", "custom", "bc_path_length_zero.pem"),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_BASIC_CONSTRAINTS
        )
        assert ext is not None
        assert ext.critical is True
        assert ext.value.ca is True
        assert ext.value.path_length == 0

    def test_ca_true_no_pathlen(self, backend):
        cert = _load_cert(
            os.path.join("x509", "PKITS_data", "certs", "GoodCACert.crt"),
            x509.load_der_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_BASIC_CONSTRAINTS
        )
        assert ext is not None
        assert ext.critical is True
        assert ext.value.ca is True
        assert ext.value.path_length is None

    def test_ca_false(self, backend):
        cert = _load_cert(
            os.path.join("x509", "cryptography.io.pem"),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_BASIC_CONSTRAINTS
        )
        assert ext is not None
        assert ext.critical is True
        assert ext.value.ca is False
        assert ext.value.path_length is None

    def test_no_basic_constraints(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509",
                "PKITS_data",
                "certs",
                "ValidCertificatePathTest1EE.crt"
            ),
            x509.load_der_x509_certificate,
            backend
        )
        with pytest.raises(x509.ExtensionNotFound):
            cert.extensions.get_extension_for_oid(x509.OID_BASIC_CONSTRAINTS)

    def test_basic_constraint_not_critical(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "basic_constraints_not_critical.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_BASIC_CONSTRAINTS
        )
        assert ext is not None
        assert ext.critical is False
        assert ext.value.ca is False


@pytest.mark.requires_backend_interface(interface=RSABackend)
@pytest.mark.requires_backend_interface(interface=X509Backend)
class TestSubjectKeyIdentifierExtension(object):
    def test_subject_key_identifier(self, backend):
        cert = _load_cert(
            os.path.join("x509", "PKITS_data", "certs", "GoodCACert.crt"),
            x509.load_der_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_SUBJECT_KEY_IDENTIFIER
        )
        ski = ext.value
        assert ext is not None
        assert ext.critical is False
        assert ski.digest == binascii.unhexlify(
            b"580184241bbc2b52944a3da510721451f5af3ac9"
        )

    def test_no_subject_key_identifier(self, backend):
        cert = _load_cert(
            os.path.join("x509", "custom", "bc_path_length_zero.pem"),
            x509.load_pem_x509_certificate,
            backend
        )
        with pytest.raises(x509.ExtensionNotFound):
            cert.extensions.get_extension_for_oid(
                x509.OID_SUBJECT_KEY_IDENTIFIER
            )


@pytest.mark.requires_backend_interface(interface=RSABackend)
@pytest.mark.requires_backend_interface(interface=X509Backend)
class TestKeyUsageExtension(object):
    def test_no_key_usage(self, backend):
        cert = _load_cert(
            os.path.join("x509", "verisign_md2_root.pem"),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions
        with pytest.raises(x509.ExtensionNotFound) as exc:
            ext.get_extension_for_oid(x509.OID_KEY_USAGE)

        assert exc.value.oid == x509.OID_KEY_USAGE

    def test_all_purposes(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "all_key_usages.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )
        extensions = cert.extensions
        ext = extensions.get_extension_for_oid(x509.OID_KEY_USAGE)
        assert ext is not None

        ku = ext.value
        assert ku.digital_signature is True
        assert ku.content_commitment is True
        assert ku.key_encipherment is True
        assert ku.data_encipherment is True
        assert ku.key_agreement is True
        assert ku.key_cert_sign is True
        assert ku.crl_sign is True
        assert ku.encipher_only is True
        assert ku.decipher_only is True

    def test_key_cert_sign_crl_sign(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "PKITS_data", "certs", "pathLenConstraint6CACert.crt"
            ),
            x509.load_der_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(x509.OID_KEY_USAGE)
        assert ext is not None
        assert ext.critical is True

        ku = ext.value
        assert ku.digital_signature is False
        assert ku.content_commitment is False
        assert ku.key_encipherment is False
        assert ku.data_encipherment is False
        assert ku.key_agreement is False
        assert ku.key_cert_sign is True
        assert ku.crl_sign is True


@pytest.mark.parametrize(
    "name", [
        x509.RFC822Name,
        x509.DNSName,
        x509.UniformResourceIdentifier
    ]
)
class TestTextGeneralNames(object):
    def test_not_text(self, name):
        with pytest.raises(TypeError):
            name(b"notaunicodestring")

        with pytest.raises(TypeError):
            name(1.3)

    def test_repr(self, name):
        gn = name(u"string")
        assert repr(gn) == "<{0}(value=string)>".format(name.__name__)

    def test_eq(self, name):
        gn = name(u"string")
        gn2 = name(u"string")
        assert gn == gn2

    def test_ne(self, name):
        gn = name(u"string")
        gn2 = name(u"string2")
        assert gn != gn2
        assert gn != object()


class TestDirectoryName(object):
    def test_not_name(self):
        with pytest.raises(TypeError):
            x509.DirectoryName(b"notaname")

        with pytest.raises(TypeError):
            x509.DirectoryName(1.3)

    def test_repr(self):
        name = x509.Name([x509.NameAttribute(x509.OID_COMMON_NAME, 'value1')])
        gn = x509.DirectoryName(x509.Name([name]))
        assert repr(gn) == (
            "<DirectoryName(value=<Name([<Name([<NameAttribute(oid=<ObjectIden"
            "tifier(oid=2.5.4.3, name=commonName)>, value='value1')>])>])>)>"
        )

    def test_eq(self):
        name = x509.Name([
            x509.NameAttribute(x509.ObjectIdentifier('oid'), 'value1')
        ])
        name2 = x509.Name([
            x509.NameAttribute(x509.ObjectIdentifier('oid'), 'value1')
        ])
        gn = x509.DirectoryName(x509.Name([name]))
        gn2 = x509.DirectoryName(x509.Name([name2]))
        assert gn == gn2

    def test_ne(self):
        name = x509.Name([
            x509.NameAttribute(x509.ObjectIdentifier('oid'), 'value1')
        ])
        name2 = x509.Name([
            x509.NameAttribute(x509.ObjectIdentifier('oid'), 'value2')
        ])
        gn = x509.DirectoryName(x509.Name([name]))
        gn2 = x509.DirectoryName(x509.Name([name2]))
        assert gn != gn2
        assert gn != object()


class TestRegisteredID(object):
    def test_not_oid(self):
        with pytest.raises(TypeError):
            x509.RegisteredID(b"notanoid")

        with pytest.raises(TypeError):
            x509.RegisteredID(1.3)

    def test_repr(self):
        gn = x509.RegisteredID(x509.OID_COMMON_NAME)
        assert repr(gn) == (
            "<RegisteredID(value=<ObjectIdentifier(oid=2.5.4.3, name=commonNam"
            "e)>)>"
        )

    def test_eq(self):
        gn = x509.RegisteredID(x509.OID_COMMON_NAME)
        gn2 = x509.RegisteredID(x509.OID_COMMON_NAME)
        assert gn == gn2

    def test_ne(self):
        gn = x509.RegisteredID(x509.OID_COMMON_NAME)
        gn2 = x509.RegisteredID(x509.OID_BASIC_CONSTRAINTS)
        assert gn != gn2
        assert gn != object()


class TestIPAddress(object):
    def test_not_ipaddress(self):
        with pytest.raises(TypeError):
            x509.IPAddress(b"notanipaddress")

        with pytest.raises(TypeError):
            x509.IPAddress(1.3)

    def test_repr(self):
        gn = x509.IPAddress(ipaddress.IPv4Address(u"127.0.0.1"))
        assert repr(gn) == "<IPAddress(value=127.0.0.1)>"

        gn2 = x509.IPAddress(ipaddress.IPv6Address(u"ff::"))
        assert repr(gn2) == "<IPAddress(value=ff::)>"

    def test_eq(self):
        gn = x509.IPAddress(ipaddress.IPv4Address(u"127.0.0.1"))
        gn2 = x509.IPAddress(ipaddress.IPv4Address(u"127.0.0.1"))
        assert gn == gn2

    def test_ne(self):
        gn = x509.IPAddress(ipaddress.IPv4Address(u"127.0.0.1"))
        gn2 = x509.IPAddress(ipaddress.IPv4Address(u"127.0.0.2"))
        assert gn != gn2
        assert gn != object()


class TestSubjectAlternativeName(object):
    def test_get_values_for_type(self):
        san = x509.SubjectAlternativeName(
            [x509.DNSName(u"cryptography.io")]
        )
        names = san.get_values_for_type(x509.DNSName)
        assert names == [u"cryptography.io"]

    def test_iter_names(self):
        san = x509.SubjectAlternativeName([
            x509.DNSName(u"cryptography.io"),
            x509.DNSName(u"crypto.local"),
        ])
        assert len(san) == 2
        assert list(san) == [
            x509.DNSName(u"cryptography.io"),
            x509.DNSName(u"crypto.local"),
        ]

    def test_invalid_general_names(self):
        with pytest.raises(TypeError):
            x509.SubjectAlternativeName(
                [x509.DNSName(u"cryptography.io"), "invalid"]
            )

    def test_repr(self):
        san = x509.SubjectAlternativeName(
            [
                x509.DNSName(u"cryptography.io")
            ]
        )
        assert repr(san) == (
            "<SubjectAlternativeName([<DNSName(value=cryptography.io)>])>"
        )

    def test_eq(self):
        san = x509.SubjectAlternativeName(
            [x509.DNSName(u"cryptography.io")]
        )
        san2 = x509.SubjectAlternativeName(
            [x509.DNSName(u"cryptography.io")]
        )
        assert san == san2

    def test_ne(self):
        san = x509.SubjectAlternativeName(
            [x509.DNSName(u"cryptography.io")]
        )
        san2 = x509.SubjectAlternativeName(
            [x509.RFC822Name(u"admin@cryptography.io")]
        )
        assert san != san2
        assert san != object()


@pytest.mark.requires_backend_interface(interface=RSABackend)
@pytest.mark.requires_backend_interface(interface=X509Backend)
class TestRSASubjectAlternativeNameExtension(object):
    def test_dns_name(self, backend):
        cert = _load_cert(
            os.path.join("x509", "cryptography.io.pem"),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_SUBJECT_ALTERNATIVE_NAME
        )
        assert ext is not None
        assert ext.critical is False

        san = ext.value

        dns = san.get_values_for_type(x509.DNSName)
        assert dns == [u"www.cryptography.io", u"cryptography.io"]

    def test_unsupported_other_name(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "san_other_name.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )
        with pytest.raises(x509.UnsupportedGeneralNameType) as exc:
            cert.extensions

        assert exc.value.type == 0

    def test_registered_id(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "san_registered_id.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_SUBJECT_ALTERNATIVE_NAME
        )
        assert ext is not None
        assert ext.critical is False

        san = ext.value
        rid = san.get_values_for_type(x509.RegisteredID)
        assert rid == [x509.ObjectIdentifier("1.2.3.4")]

    def test_uri(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "san_uri_with_port.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_SUBJECT_ALTERNATIVE_NAME
        )
        assert ext is not None
        uri = ext.value.get_values_for_type(
            x509.UniformResourceIdentifier
        )
        assert uri == [
            u"gopher://\u043f\u044b\u043a\u0430.cryptography:70/path?q=s#hel"
            u"lo",
            u"http://someregulardomain.com",
        ]

    def test_ipaddress(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "san_ipaddr.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_SUBJECT_ALTERNATIVE_NAME
        )
        assert ext is not None
        assert ext.critical is False

        san = ext.value

        ip = san.get_values_for_type(x509.IPAddress)
        assert [
            ipaddress.ip_address(u"127.0.0.1"),
            ipaddress.ip_address(u"ff::")
        ] == ip

    def test_dirname(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "san_dirname.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_SUBJECT_ALTERNATIVE_NAME
        )
        assert ext is not None
        assert ext.critical is False

        san = ext.value

        dirname = san.get_values_for_type(x509.DirectoryName)
        assert [
            x509.Name([
                x509.NameAttribute(x509.OID_COMMON_NAME, 'test'),
                x509.NameAttribute(x509.OID_ORGANIZATION_NAME, 'Org'),
                x509.NameAttribute(x509.OID_STATE_OR_PROVINCE_NAME, 'Texas'),
            ])
        ] == dirname

    def test_rfc822name(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "san_rfc822_idna.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_SUBJECT_ALTERNATIVE_NAME
        )
        assert ext is not None
        assert ext.critical is False

        san = ext.value

        rfc822name = san.get_values_for_type(x509.RFC822Name)
        assert [u"email@em\xe5\xefl.com"] == rfc822name

    def test_unicode_rfc822_name_dns_name_uri(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "san_idna_names.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_SUBJECT_ALTERNATIVE_NAME
        )
        assert ext is not None
        rfc822_name = ext.value.get_values_for_type(x509.RFC822Name)
        dns_name = ext.value.get_values_for_type(x509.DNSName)
        uri = ext.value.get_values_for_type(x509.UniformResourceIdentifier)
        assert rfc822_name == [u"email@\u043f\u044b\u043a\u0430.cryptography"]
        assert dns_name == [u"\u043f\u044b\u043a\u0430.cryptography"]
        assert uri == [u"https://www.\u043f\u044b\u043a\u0430.cryptography"]

    def test_rfc822name_dnsname_ipaddress_directoryname_uri(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "san_email_dns_ip_dirname_uri.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_SUBJECT_ALTERNATIVE_NAME
        )
        assert ext is not None
        assert ext.critical is False

        san = ext.value

        rfc822_name = san.get_values_for_type(x509.RFC822Name)
        uri = san.get_values_for_type(x509.UniformResourceIdentifier)
        dns = san.get_values_for_type(x509.DNSName)
        ip = san.get_values_for_type(x509.IPAddress)
        dirname = san.get_values_for_type(x509.DirectoryName)
        assert [u"user@cryptography.io"] == rfc822_name
        assert [u"https://cryptography.io"] == uri
        assert [u"cryptography.io"] == dns
        assert [
            x509.Name([
                x509.NameAttribute(x509.OID_COMMON_NAME, 'dirCN'),
                x509.NameAttribute(
                    x509.OID_ORGANIZATION_NAME, 'Cryptographic Authority'
                ),
            ])
        ] == dirname
        assert [
            ipaddress.ip_address(u"127.0.0.1"),
            ipaddress.ip_address(u"ff::")
        ] == ip

    def test_invalid_rfc822name(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "san_rfc822_names.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )
        with pytest.raises(ValueError) as exc:
            cert.extensions

        assert 'Invalid rfc822name value' in str(exc.value)


@pytest.mark.requires_backend_interface(interface=RSABackend)
@pytest.mark.requires_backend_interface(interface=X509Backend)
class TestExtendedKeyUsageExtension(object):
    def test_eku(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "extended_key_usage.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_EXTENDED_KEY_USAGE
        )
        assert ext is not None
        assert ext.critical is False

        assert [
            x509.ObjectIdentifier("1.3.6.1.5.5.7.3.1"),
            x509.ObjectIdentifier("1.3.6.1.5.5.7.3.2"),
            x509.ObjectIdentifier("1.3.6.1.5.5.7.3.3"),
            x509.ObjectIdentifier("1.3.6.1.5.5.7.3.4"),
            x509.ObjectIdentifier("1.3.6.1.5.5.7.3.9"),
            x509.ObjectIdentifier("1.3.6.1.5.5.7.3.8"),
            x509.ObjectIdentifier("2.5.29.37.0"),
            x509.ObjectIdentifier("2.16.840.1.113730.4.1"),
        ] == list(ext.value)


class TestAccessDescription(object):
    def test_invalid_access_method(self):
        with pytest.raises(ValueError):
            x509.AccessDescription("notanoid", x509.DNSName(u"test"))

    def test_invalid_access_location(self):
        with pytest.raises(TypeError):
            x509.AccessDescription(x509.OID_CA_ISSUERS, "invalid")

    def test_repr(self):
        ad = x509.AccessDescription(
            x509.OID_OCSP,
            x509.UniformResourceIdentifier(u"http://ocsp.domain.com")
        )
        assert repr(ad) == (
            "<AccessDescription(access_method=<ObjectIdentifier(oid=1.3.6.1.5."
            "5.7.48.1, name=OCSP)>, access_location=<UniformResourceIdentifier"
            "(value=http://ocsp.domain.com)>)>"
        )

    def test_eq(self):
        ad = x509.AccessDescription(
            x509.OID_OCSP,
            x509.UniformResourceIdentifier(u"http://ocsp.domain.com")
        )
        ad2 = x509.AccessDescription(
            x509.OID_OCSP,
            x509.UniformResourceIdentifier(u"http://ocsp.domain.com")
        )
        assert ad == ad2

    def test_ne(self):
        ad = x509.AccessDescription(
            x509.OID_OCSP,
            x509.UniformResourceIdentifier(u"http://ocsp.domain.com")
        )
        ad2 = x509.AccessDescription(
            x509.OID_CA_ISSUERS,
            x509.UniformResourceIdentifier(u"http://ocsp.domain.com")
        )
        ad3 = x509.AccessDescription(
            x509.OID_OCSP,
            x509.UniformResourceIdentifier(u"http://notthesame")
        )
        assert ad != ad2
        assert ad != ad3
        assert ad != object()


class TestAuthorityInformationAccess(object):
    def test_invalid_descriptions(self):
        with pytest.raises(TypeError):
            x509.AuthorityInformationAccess(["notanAccessDescription"])

    def test_iter_len(self):
        aia = x509.AuthorityInformationAccess([
            x509.AccessDescription(
                x509.OID_OCSP,
                x509.UniformResourceIdentifier(u"http://ocsp.domain.com")
            ),
            x509.AccessDescription(
                x509.OID_CA_ISSUERS,
                x509.UniformResourceIdentifier(u"http://domain.com/ca.crt")
            )
        ])
        assert len(aia) == 2
        assert list(aia) == [
            x509.AccessDescription(
                x509.OID_OCSP,
                x509.UniformResourceIdentifier(u"http://ocsp.domain.com")
            ),
            x509.AccessDescription(
                x509.OID_CA_ISSUERS,
                x509.UniformResourceIdentifier(u"http://domain.com/ca.crt")
            )
        ]

    def test_repr(self):
        aia = x509.AuthorityInformationAccess([
            x509.AccessDescription(
                x509.OID_OCSP,
                x509.UniformResourceIdentifier(u"http://ocsp.domain.com")
            ),
            x509.AccessDescription(
                x509.OID_CA_ISSUERS,
                x509.UniformResourceIdentifier(u"http://domain.com/ca.crt")
            )
        ])
        assert repr(aia) == (
            "<AuthorityInformationAccess([<AccessDescription(access_method=<Ob"
            "jectIdentifier(oid=1.3.6.1.5.5.7.48.1, name=OCSP)>, access_locati"
            "on=<UniformResourceIdentifier(value=http://ocsp.domain.com)>)>, <"
            "AccessDescription(access_method=<ObjectIdentifier(oid=1.3.6.1.5.5"
            ".7.48.2, name=caIssuers)>, access_location=<UniformResourceIdenti"
            "fier(value=http://domain.com/ca.crt)>)>])>"
        )

    def test_eq(self):
        aia = x509.AuthorityInformationAccess([
            x509.AccessDescription(
                x509.OID_OCSP,
                x509.UniformResourceIdentifier(u"http://ocsp.domain.com")
            ),
            x509.AccessDescription(
                x509.OID_CA_ISSUERS,
                x509.UniformResourceIdentifier(u"http://domain.com/ca.crt")
            )
        ])
        aia2 = x509.AuthorityInformationAccess([
            x509.AccessDescription(
                x509.OID_OCSP,
                x509.UniformResourceIdentifier(u"http://ocsp.domain.com")
            ),
            x509.AccessDescription(
                x509.OID_CA_ISSUERS,
                x509.UniformResourceIdentifier(u"http://domain.com/ca.crt")
            )
        ])
        assert aia == aia2

    def test_ne(self):
        aia = x509.AuthorityInformationAccess([
            x509.AccessDescription(
                x509.OID_OCSP,
                x509.UniformResourceIdentifier(u"http://ocsp.domain.com")
            ),
            x509.AccessDescription(
                x509.OID_CA_ISSUERS,
                x509.UniformResourceIdentifier(u"http://domain.com/ca.crt")
            )
        ])
        aia2 = x509.AuthorityInformationAccess([
            x509.AccessDescription(
                x509.OID_OCSP,
                x509.UniformResourceIdentifier(u"http://ocsp.domain.com")
            ),
        ])

        assert aia != aia2
        assert aia != object()


@pytest.mark.requires_backend_interface(interface=RSABackend)
@pytest.mark.requires_backend_interface(interface=X509Backend)
class TestAuthorityInformationAccessExtension(object):
    def test_aia_ocsp_ca_issuers(self, backend):
        cert = _load_cert(
            os.path.join("x509", "cryptography.io.pem"),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_AUTHORITY_INFORMATION_ACCESS
        )
        assert ext is not None
        assert ext.critical is False

        assert ext.value == x509.AuthorityInformationAccess([
            x509.AccessDescription(
                x509.OID_OCSP,
                x509.UniformResourceIdentifier(u"http://gv.symcd.com")
            ),
            x509.AccessDescription(
                x509.OID_CA_ISSUERS,
                x509.UniformResourceIdentifier(u"http://gv.symcb.com/gv.crt")
            ),
        ])

    def test_aia_multiple_ocsp_ca_issuers(self, backend):
        cert = _load_cert(
            os.path.join("x509", "custom", "aia_ocsp_ca_issuers.pem"),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_AUTHORITY_INFORMATION_ACCESS
        )
        assert ext is not None
        assert ext.critical is False

        assert ext.value == x509.AuthorityInformationAccess([
            x509.AccessDescription(
                x509.OID_OCSP,
                x509.UniformResourceIdentifier(u"http://ocsp.domain.com")
            ),
            x509.AccessDescription(
                x509.OID_OCSP,
                x509.UniformResourceIdentifier(u"http://ocsp2.domain.com")
            ),
            x509.AccessDescription(
                x509.OID_CA_ISSUERS,
                x509.DirectoryName(x509.Name([
                    x509.NameAttribute(x509.OID_COMMON_NAME, "myCN"),
                    x509.NameAttribute(x509.OID_ORGANIZATION_NAME, "some Org"),
                ]))
            ),
        ])

    def test_aia_ocsp_only(self, backend):
        cert = _load_cert(
            os.path.join("x509", "custom", "aia_ocsp.pem"),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_AUTHORITY_INFORMATION_ACCESS
        )
        assert ext is not None
        assert ext.critical is False

        assert ext.value == x509.AuthorityInformationAccess([
            x509.AccessDescription(
                x509.OID_OCSP,
                x509.UniformResourceIdentifier(u"http://ocsp.domain.com")
            ),
        ])

    def test_aia_ca_issuers_only(self, backend):
        cert = _load_cert(
            os.path.join("x509", "custom", "aia_ca_issuers.pem"),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_AUTHORITY_INFORMATION_ACCESS
        )
        assert ext is not None
        assert ext.critical is False

        assert ext.value == x509.AuthorityInformationAccess([
            x509.AccessDescription(
                x509.OID_CA_ISSUERS,
                x509.DirectoryName(x509.Name([
                    x509.NameAttribute(x509.OID_COMMON_NAME, "myCN"),
                    x509.NameAttribute(x509.OID_ORGANIZATION_NAME, "some Org"),
                ]))
            ),
        ])


@pytest.mark.requires_backend_interface(interface=RSABackend)
@pytest.mark.requires_backend_interface(interface=X509Backend)
class TestAuthorityKeyIdentifierExtension(object):
    def test_aki_keyid(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "cryptography.io.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_AUTHORITY_KEY_IDENTIFIER
        )
        assert ext is not None
        assert ext.critical is False

        assert ext.value.key_identifier == (
            b"\xc3\x9c\xf3\xfc\xd3F\x084\xbb\xceF\x7f\xa0|[\xf3\xe2\x08\xcbY"
        )
        assert ext.value.authority_cert_issuer is None
        assert ext.value.authority_cert_serial_number is None

    def test_aki_all_fields(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "authority_key_identifier.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_AUTHORITY_KEY_IDENTIFIER
        )
        assert ext is not None
        assert ext.critical is False

        assert ext.value.key_identifier == (
            b"9E>\xca=b\x1d\xea\x86I\xf6Z\xab@\xb7\xa4p\x98\xf1\xec"
        )
        assert ext.value.authority_cert_issuer == [
            x509.DirectoryName(
                x509.Name([
                    x509.NameAttribute(
                        x509.OID_ORGANIZATION_NAME, u"PyCA"
                    ),
                    x509.NameAttribute(
                        x509.OID_COMMON_NAME, u"cryptography.io"
                    )
                ])
            )
        ]
        assert ext.value.authority_cert_serial_number == 3

    def test_aki_no_keyid(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "authority_key_identifier_no_keyid.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )
        ext = cert.extensions.get_extension_for_oid(
            x509.OID_AUTHORITY_KEY_IDENTIFIER
        )
        assert ext is not None
        assert ext.critical is False

        assert ext.value.key_identifier is None
        assert ext.value.authority_cert_issuer == [
            x509.DirectoryName(
                x509.Name([
                    x509.NameAttribute(
                        x509.OID_ORGANIZATION_NAME, u"PyCA"
                    ),
                    x509.NameAttribute(
                        x509.OID_COMMON_NAME, u"cryptography.io"
                    )
                ])
            )
        ]
        assert ext.value.authority_cert_serial_number == 3


class TestDistributionPoint(object):
    def test_distribution_point_full_name_not_general_names(self):
        with pytest.raises(TypeError):
            x509.DistributionPoint(["notgn"], None, None, None)

    def test_distribution_point_relative_name_not_name(self):
        with pytest.raises(TypeError):
            x509.DistributionPoint(None, "notname", None, None)

    def test_distribution_point_full_and_relative_not_none(self):
        with pytest.raises(ValueError):
            x509.DistributionPoint("data", "notname", None, None)

    def test_crl_issuer_not_general_names(self):
        with pytest.raises(TypeError):
            x509.DistributionPoint(None, None, None, ["notgn"])

    def test_reason_not_reasonflags(self):
        with pytest.raises(TypeError):
            x509.DistributionPoint(
                [x509.UniformResourceIdentifier(u"http://crypt.og/crl")],
                None,
                frozenset(["notreasonflags"]),
                None
            )

    def test_reason_not_frozenset(self):
        with pytest.raises(TypeError):
            x509.DistributionPoint(
                [x509.UniformResourceIdentifier(u"http://crypt.og/crl")],
                None,
                [x509.ReasonFlags.ca_compromise],
                None
            )

    def test_disallowed_reasons(self):
        with pytest.raises(ValueError):
            x509.DistributionPoint(
                [x509.UniformResourceIdentifier(u"http://crypt.og/crl")],
                None,
                frozenset([x509.ReasonFlags.unspecified]),
                None
            )

        with pytest.raises(ValueError):
            x509.DistributionPoint(
                [x509.UniformResourceIdentifier(u"http://crypt.og/crl")],
                None,
                frozenset([x509.ReasonFlags.remove_from_crl]),
                None
            )

    def test_reason_only(self):
        with pytest.raises(ValueError):
            x509.DistributionPoint(
                None,
                None,
                frozenset([x509.ReasonFlags.aa_compromise]),
                None
            )

    def test_eq(self):
        dp = x509.DistributionPoint(
            [x509.UniformResourceIdentifier(u"http://crypt.og/crl")],
            None,
            frozenset([x509.ReasonFlags.superseded]),
            [
                x509.DirectoryName(
                    x509.Name([
                        x509.NameAttribute(
                            x509.OID_COMMON_NAME, "Important CA"
                        )
                    ])
                )
            ],
        )
        dp2 = x509.DistributionPoint(
            [x509.UniformResourceIdentifier(u"http://crypt.og/crl")],
            None,
            frozenset([x509.ReasonFlags.superseded]),
            [
                x509.DirectoryName(
                    x509.Name([
                        x509.NameAttribute(
                            x509.OID_COMMON_NAME, "Important CA"
                        )
                    ])
                )
            ],
        )
        assert dp == dp2

    def test_ne(self):
        dp = x509.DistributionPoint(
            [x509.UniformResourceIdentifier(u"http://crypt.og/crl")],
            None,
            frozenset([x509.ReasonFlags.superseded]),
            [
                x509.DirectoryName(
                    x509.Name([
                        x509.NameAttribute(
                            x509.OID_COMMON_NAME, "Important CA"
                        )
                    ])
                )
            ],
        )
        dp2 = x509.DistributionPoint(
            [x509.UniformResourceIdentifier(u"http://crypt.og/crl")],
            None,
            None,
            None
        )
        assert dp != dp2
        assert dp != object()

    def test_repr(self):
        dp = x509.DistributionPoint(
            None,
            x509.Name([
                x509.NameAttribute(x509.OID_COMMON_NAME, "myCN")
            ]),
            frozenset([x509.ReasonFlags.ca_compromise]),
            [
                x509.DirectoryName(
                    x509.Name([
                        x509.NameAttribute(
                            x509.OID_COMMON_NAME, "Important CA"
                        )
                    ])
                )
            ],
        )
        if six.PY3:
            assert repr(dp) == (
                "<DistributionPoint(full_name=None, relative_name=<Name([<Name"
                "Attribute(oid=<ObjectIdentifier(oid=2.5.4.3, name=commonName)"
                ">, value='myCN')>])>, reasons=frozenset({<ReasonFlags.ca_comp"
                "romise: 'cACompromise'>}), crl_issuer=[<DirectoryName(value=<"
                "Name([<NameAttribute(oid=<ObjectIdentifier(oid=2.5.4.3, name="
                "commonName)>, value='Important CA')>])>)>])>"
            )
        else:
            assert repr(dp) == (
                "<DistributionPoint(full_name=None, relative_name=<Name([<Name"
                "Attribute(oid=<ObjectIdentifier(oid=2.5.4.3, name=commonName)"
                ">, value='myCN')>])>, reasons=frozenset([<ReasonFlags.ca_comp"
                "romise: 'cACompromise'>]), crl_issuer=[<DirectoryName(value=<"
                "Name([<NameAttribute(oid=<ObjectIdentifier(oid=2.5.4.3, name="
                "commonName)>, value='Important CA')>])>)>])>"
            )


class TestCRLDistributionPoints(object):
    def test_invalid_distribution_points(self):
        with pytest.raises(TypeError):
            x509.CRLDistributionPoints(["notadistributionpoint"])

    def test_iter_len(self):
        cdp = x509.CRLDistributionPoints([
            x509.DistributionPoint(
                [x509.UniformResourceIdentifier(u"http://domain")],
                None,
                None,
                None
            ),
            x509.DistributionPoint(
                [x509.UniformResourceIdentifier(u"ftp://domain")],
                None,
                frozenset([
                    x509.ReasonFlags.key_compromise,
                    x509.ReasonFlags.ca_compromise,
                ]),
                None
            ),
        ])
        assert len(cdp) == 2
        assert list(cdp) == [
            x509.DistributionPoint(
                [x509.UniformResourceIdentifier(u"http://domain")],
                None,
                None,
                None
            ),
            x509.DistributionPoint(
                [x509.UniformResourceIdentifier(u"ftp://domain")],
                None,
                frozenset([
                    x509.ReasonFlags.key_compromise,
                    x509.ReasonFlags.ca_compromise,
                ]),
                None
            ),
        ]

    def test_repr(self):
        cdp = x509.CRLDistributionPoints([
            x509.DistributionPoint(
                [x509.UniformResourceIdentifier(u"ftp://domain")],
                None,
                frozenset([x509.ReasonFlags.key_compromise]),
                None
            ),
        ])
        if six.PY3:
            assert repr(cdp) == (
                "<CRLDistributionPoints([<DistributionPoint(full_name=[<Unifo"
                "rmResourceIdentifier(value=ftp://domain)>], relative_name=No"
                "ne, reasons=frozenset({<ReasonFlags.key_compromise: 'keyComp"
                "romise'>}), crl_issuer=None)>])>"
            )
        else:
            assert repr(cdp) == (
                "<CRLDistributionPoints([<DistributionPoint(full_name=[<Unifo"
                "rmResourceIdentifier(value=ftp://domain)>], relative_name=No"
                "ne, reasons=frozenset([<ReasonFlags.key_compromise: 'keyComp"
                "romise'>]), crl_issuer=None)>])>"
            )

    def test_eq(self):
        cdp = x509.CRLDistributionPoints([
            x509.DistributionPoint(
                [x509.UniformResourceIdentifier(u"ftp://domain")],
                None,
                frozenset([
                    x509.ReasonFlags.key_compromise,
                    x509.ReasonFlags.ca_compromise,
                ]),
                [x509.UniformResourceIdentifier(u"uri://thing")],
            ),
        ])
        cdp2 = x509.CRLDistributionPoints([
            x509.DistributionPoint(
                [x509.UniformResourceIdentifier(u"ftp://domain")],
                None,
                frozenset([
                    x509.ReasonFlags.key_compromise,
                    x509.ReasonFlags.ca_compromise,
                ]),
                [x509.UniformResourceIdentifier(u"uri://thing")],
            ),
        ])
        assert cdp == cdp2

    def test_ne(self):
        cdp = x509.CRLDistributionPoints([
            x509.DistributionPoint(
                [x509.UniformResourceIdentifier(u"ftp://domain")],
                None,
                frozenset([
                    x509.ReasonFlags.key_compromise,
                    x509.ReasonFlags.ca_compromise,
                ]),
                [x509.UniformResourceIdentifier(u"uri://thing")],
            ),
        ])
        cdp2 = x509.CRLDistributionPoints([
            x509.DistributionPoint(
                [x509.UniformResourceIdentifier(u"ftp://domain2")],
                None,
                frozenset([
                    x509.ReasonFlags.key_compromise,
                    x509.ReasonFlags.ca_compromise,
                ]),
                [x509.UniformResourceIdentifier(u"uri://thing")],
            ),
        ])
        cdp3 = x509.CRLDistributionPoints([
            x509.DistributionPoint(
                [x509.UniformResourceIdentifier(u"ftp://domain")],
                None,
                frozenset([x509.ReasonFlags.key_compromise]),
                [x509.UniformResourceIdentifier(u"uri://thing")],
            ),
        ])
        cdp4 = x509.CRLDistributionPoints([
            x509.DistributionPoint(
                [x509.UniformResourceIdentifier(u"ftp://domain")],
                None,
                frozenset([
                    x509.ReasonFlags.key_compromise,
                    x509.ReasonFlags.ca_compromise,
                ]),
                [x509.UniformResourceIdentifier(u"uri://thing2")],
            ),
        ])
        assert cdp != cdp2
        assert cdp != cdp3
        assert cdp != cdp4
        assert cdp != object()


@pytest.mark.requires_backend_interface(interface=RSABackend)
@pytest.mark.requires_backend_interface(interface=X509Backend)
class TestCRLDistributionPointsExtension(object):
    def test_fullname_and_crl_issuer(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "PKITS_data", "certs", "ValidcRLIssuerTest28EE.crt"
            ),
            x509.load_der_x509_certificate,
            backend
        )

        cdps = cert.extensions.get_extension_for_oid(
            x509.OID_CRL_DISTRIBUTION_POINTS
        ).value

        assert cdps == x509.CRLDistributionPoints([
            x509.DistributionPoint(
                full_name=[x509.DirectoryName(
                    x509.Name([
                        x509.NameAttribute(x509.OID_COUNTRY_NAME, "US"),
                        x509.NameAttribute(
                            x509.OID_ORGANIZATION_NAME,
                            "Test Certificates 2011"
                        ),
                        x509.NameAttribute(
                            x509.OID_ORGANIZATIONAL_UNIT_NAME,
                            "indirectCRL CA3 cRLIssuer"
                        ),
                        x509.NameAttribute(
                            x509.OID_COMMON_NAME,
                            "indirect CRL for indirectCRL CA3"
                        ),
                    ])
                )],
                relative_name=None,
                reasons=None,
                crl_issuer=[x509.DirectoryName(
                    x509.Name([
                        x509.NameAttribute(x509.OID_COUNTRY_NAME, "US"),
                        x509.NameAttribute(
                            x509.OID_ORGANIZATION_NAME,
                            "Test Certificates 2011"
                        ),
                        x509.NameAttribute(
                            x509.OID_ORGANIZATIONAL_UNIT_NAME,
                            "indirectCRL CA3 cRLIssuer"
                        ),
                    ])
                )],
            )
        ])

    def test_relativename_and_crl_issuer(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "PKITS_data", "certs", "ValidcRLIssuerTest29EE.crt"
            ),
            x509.load_der_x509_certificate,
            backend
        )

        cdps = cert.extensions.get_extension_for_oid(
            x509.OID_CRL_DISTRIBUTION_POINTS
        ).value

        assert cdps == x509.CRLDistributionPoints([
            x509.DistributionPoint(
                full_name=None,
                relative_name=x509.Name([
                    x509.NameAttribute(
                        x509.OID_COMMON_NAME,
                        "indirect CRL for indirectCRL CA3"
                    ),
                ]),
                reasons=None,
                crl_issuer=[x509.DirectoryName(
                    x509.Name([
                        x509.NameAttribute(x509.OID_COUNTRY_NAME, "US"),
                        x509.NameAttribute(
                            x509.OID_ORGANIZATION_NAME,
                            "Test Certificates 2011"
                        ),
                        x509.NameAttribute(
                            x509.OID_ORGANIZATIONAL_UNIT_NAME,
                            "indirectCRL CA3 cRLIssuer"
                        ),
                    ])
                )],
            )
        ])

    def test_fullname_crl_issuer_reasons(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "cdp_fullname_reasons_crl_issuer.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )

        cdps = cert.extensions.get_extension_for_oid(
            x509.OID_CRL_DISTRIBUTION_POINTS
        ).value

        assert cdps == x509.CRLDistributionPoints([
            x509.DistributionPoint(
                full_name=[x509.UniformResourceIdentifier(
                    u"http://myhost.com/myca.crl"
                )],
                relative_name=None,
                reasons=frozenset([
                    x509.ReasonFlags.key_compromise,
                    x509.ReasonFlags.ca_compromise
                ]),
                crl_issuer=[x509.DirectoryName(
                    x509.Name([
                        x509.NameAttribute(x509.OID_COUNTRY_NAME, "US"),
                        x509.NameAttribute(
                            x509.OID_ORGANIZATION_NAME, "PyCA"
                        ),
                        x509.NameAttribute(
                            x509.OID_COMMON_NAME, "cryptography CA"
                        ),
                    ])
                )],
            )
        ])

    def test_all_reasons(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "cdp_all_reasons.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )

        cdps = cert.extensions.get_extension_for_oid(
            x509.OID_CRL_DISTRIBUTION_POINTS
        ).value

        assert cdps == x509.CRLDistributionPoints([
            x509.DistributionPoint(
                full_name=[x509.UniformResourceIdentifier(
                    u"http://domain.com/some.crl"
                )],
                relative_name=None,
                reasons=frozenset([
                    x509.ReasonFlags.key_compromise,
                    x509.ReasonFlags.ca_compromise,
                    x509.ReasonFlags.affiliation_changed,
                    x509.ReasonFlags.superseded,
                    x509.ReasonFlags.privilege_withdrawn,
                    x509.ReasonFlags.cessation_of_operation,
                    x509.ReasonFlags.aa_compromise,
                    x509.ReasonFlags.certificate_hold,
                ]),
                crl_issuer=None
            )
        ])

    def test_single_reason(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "cdp_reason_aa_compromise.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )

        cdps = cert.extensions.get_extension_for_oid(
            x509.OID_CRL_DISTRIBUTION_POINTS
        ).value

        assert cdps == x509.CRLDistributionPoints([
            x509.DistributionPoint(
                full_name=[x509.UniformResourceIdentifier(
                    u"http://domain.com/some.crl"
                )],
                relative_name=None,
                reasons=frozenset([x509.ReasonFlags.aa_compromise]),
                crl_issuer=None
            )
        ])

    def test_crl_issuer_only(self, backend):
        cert = _load_cert(
            os.path.join(
                "x509", "custom", "cdp_crl_issuer.pem"
            ),
            x509.load_pem_x509_certificate,
            backend
        )

        cdps = cert.extensions.get_extension_for_oid(
            x509.OID_CRL_DISTRIBUTION_POINTS
        ).value

        assert cdps == x509.CRLDistributionPoints([
            x509.DistributionPoint(
                full_name=None,
                relative_name=None,
                reasons=None,
                crl_issuer=[x509.DirectoryName(
                    x509.Name([
                        x509.NameAttribute(
                            x509.OID_COMMON_NAME, "cryptography CA"
                        ),
                    ])
                )],
            )
        ])
