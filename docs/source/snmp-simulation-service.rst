
.. _snmp-simulation-service:

SNMP simulation service
=======================

SNMP Labs hosts an SNMP Simulator instance on
`Digital Ocean <https://cloud.digitalocean.com/>`_ cloud in
hope to help fellow software developers that are looking to test their
SNMP code against live SNMP agents of different kinds.

Please, note that this service is provided as-is without any guarantees on its
reliability and correctness. Its use is generally covered
by SNMP Simulator :doc:`/license`.

If you are considering Digital Ocean as a cloud service provider for your own
needs, `this voucher <https://m.do.co/c/debefe816df4>`_ will get you $10 credit
and also benefit SNMP Labs.

In case of any troubles or suggestions, please
`open up a <https://github.com/etingof/snmplabs.com/issues/new>`_ GitHub issue.

.. _simulated-snmp-engines:

SNMP engines
------------

There are four independent SNMP engines configured at different UDP ports:

+--------------------------------+-------------------+----------------+
| **SNMP Engine ID**             | **Hostname**      | **UDP port**   |
+--------------------------------+-------------------+----------------+
| 0x80004fb805636c6f75644dab22cc | demo.snmplabs.com | 161 (standard) |
+--------------------------------+-------------------+----------------+
| 0x80004fb805636c6f75644dab22cd | demo.snmplabs.com | 1161           |
+--------------------------------+-------------------+----------------+
| 0x80004fb805636c6f75644dab22ce | demo.snmplabs.com | 2161           |
+--------------------------------+-------------------+----------------+
| 0x80004fb805636c6f75644dab22cf | demo.snmplabs.com | 3161           |
+--------------------------------+-------------------+----------------+

.. note::

   The simulation service is implemented by two independent UNIX processes.
   One process runs the first SNMP engine (*0x80004fb805636c6f75644dab22cc*)
   while the rest of SNMP engines in the table above are all local to the
   second SNMP simulator process.

.. _simulated-community-names:

SNMPv1/v2c communities
----------------------

Each of the :ref:`SNMP engines <simulated-snmp-engines>` supports a
:ref:`bunch of SNMP community names <simulated-data>` to address distinct
simulated SNMP agent.

To start with, the conventional **public** and **private** SNMP community names
are available as well.

.. _simulated-usm-users:

SNMPv3 USM
----------

Each :ref:`SNMP engine <simulated-snmp-engines>` has a bunch of USM users
configured to it. The users are named after authentication/encryption protocol
combinations for convenience.

SNMPv3 user table
+++++++++++++++++

The following table includes plain-text keys (AKA passwords or pass-phrases) used
by SNMP USM security model for cryptographic authenticaton and encryption.

+------------------------+---------------------------+----------------------+-------------------------+------------------+
| USM Security Name      | Authentication protocol   | Authentication key   | Encryption protocol     | Encryption key   |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-none-none          | -                         | -                    | -                       | -                |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-md5-none           | MD5                       | authkey1             | -                       | -                |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-md5-des            | MD5                       | authkey1             | DES                     | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-md5-3des           | MD5                       | authkey1             | Triple DES              | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-md5-aes            | MD5                       | authkey1             | AES (128bit)            | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-md5-aes128         | MD5                       | authkey1             | AES (128bit)            | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-md5-aes192         | MD5                       | authkey1             | AES Reeder (192bit)     | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-md5-aes192-blmt    | MD5                       | authkey1             | AES Blumenthal (192bit) | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-md5-aes256         | MD5                       | authkey1             | AES Reeder (256bit)     | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-md5-aes256-blmt    | MD5                       | authkey1             | AES Blumenthal (256bit) | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha-none           | SHA1 (96/160bit)          | authkey1             | -                       | -                |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha-des            | SHA1 (96/160bit)          | authkey1             | DES                     | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha-3des           | SHA1 (96/160bit)          | authkey1             | Triple DES              | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha-aes            | SHA1 (96/160bit)          | authkey1             | AES (128bit)            | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha-aes128         | SHA1 (96/160bit)          | authkey1             | AES (128bit)            | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha-aes192         | SHA1 (96/160bit)          | authkey1             | AES Reeder (192bit)     | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha-aes192-blmt    | SHA1 (96/160bit)          | authkey1             | AES Blumenthal (192bit) | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha-aes256         | SHA1 (96/160bit)          | authkey1             | AES Reeder (256bit)     | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha-aes256-blmt    | SHA1 (96/160bit)          | authkey1             | AES Blumenthal (256bit) | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha224-none        | SHA2 (128/224bit)         | authkey1             | -                       | -                |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha224-des         | SHA2 (128/224bit)         | authkey1             | DES                     | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha224-3des        | SHA2 (128/224bit)         | authkey1             | Triple DES              | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha224-aes         | SHA2 (128/224bit)         | authkey1             | AES (128bit)            | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha224-aes128      | SHA2 (128/224bit)         | authkey1             | AES (128bit)            | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha224-aes192      | SHA2 (128/224bit)         | authkey1             | AES Reeder (192bit)     | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha224-aes192-blmt | SHA2 (128/224bit)         | authkey1             | AES Blumenthal (192bit) | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha224-aes256      | SHA2 (128/224bit)         | authkey1             | AES Reeder (256bit)     | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha224-aes256-blmt | SHA2 (128/224bit)         | authkey1             | AES Blumenthal (256bit) | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha256-none        | SHA2 (192/256bit)         | authkey1             | -                       | -                |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha256-des         | SHA2 (192/256bit)         | authkey1             | DES                     | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha256-3des        | SHA2 (192/256bit)         | authkey1             | Triple DES              | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha256-aes         | SHA2 (192/256bit)         | authkey1             | AES (128bit)            | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha256-aes128      | SHA2 (192/256bit)         | authkey1             | AES (192bit)            | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha256-aes192      | SHA2 (192/256bit)         | authkey1             | AES Reeder (192bit)     | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha256-aes192-blmt | SHA2 (192/256bit)         | authkey1             | AES Blumenthal (192bit) | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha256-aes256      | SHA2 (192/256bit)         | authkey1             | AES Reeder (256bit)     | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha256-aes256-blmt | SHA2 (192/256bit)         | authkey1             | AES Blumenthal (256bit) | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha384-none        | SHA2 (256/384bit)         | authkey1             | -                       | -                |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha384-des         | SHA2 (256/384bit)         | authkey1             | DES                     | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha384-aes         | SHA2 (256/384bit)         | authkey1             | AES (128bit)            | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha384-aes128      | SHA2 (256/384bit)         | authkey1             | AES (128bit)            | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha384-aes192      | SHA2 (256/384bit)         | authkey1             | AES Reeder (192bit)     | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha384-aes192-blmt | SHA2 (256/384bit)         | authkey1             | AES Blumenthal (192bit) | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha384-aes256      | SHA2 (256/384bit)         | authkey1             | AES Reeder (256bit)     | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha384-aes256-blmt | SHA2 (256/384bit)         | authkey1             | AES Blumenthal (256bit) | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha512-none        | SHA2 (384/512bit)         | authkey1             | -                       | -                |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha512-des         | SHA2 (384/512bit)         | authkey1             | DES                     | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha512-3des        | SHA2 (384/512bit)         | authkey1             | Triple DES              | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha512-aes         | SHA2 (384/512bit)         | authkey1             | AES (128bit)            | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha512-aes192      | SHA2 (384/512bit)         | authkey1             | AES Reeder (192bit)     | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha512-aes192-blmt | SHA2 (384/512bit)         | authkey1             | AES Blumenthal (192bit) | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha512-aes256      | SHA2 (384/512bit)         | authkey1             | AES Reeder (256bit)     | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+
| usr-sha512-aes256-blmt | SHA2 (384/512bit)         | authkey1             | AES Blumenthal (256bit) | privkey1         |
+------------------------+---------------------------+----------------------+-------------------------+------------------+

.. note::

   The *Triple DES* authentication algorithm is implemented according to
   `draft-reeder-snmpv3-usm-3desede-00 <https://tools.ietf.org/html/draft-reeder-snmpv3-usm-3desede-00#section-5>`_.
   The AES-based privacy algorithms with key size 192bit+ are implemented along the lines of
   `draft-blumenthal-aes-usm-04 <https://tools.ietf.org/html/draft-blumenthal-aes-usm-04#section-3>`_)
   with either Reeder or Blumenthal  key localization.

.. _master_and_localized_keys:

Master and localized keys
+++++++++++++++++++++++++

Internally, SNMP USM stores hashes of the plain-text keys in two forms:

* Hashed plain-text key, which is frequently referred to as a *master key*
* Master key hashed with SNMP engine ID of the authoritative (i.e. "owning"
  management information) SNMP entity, which is known as a *localized key*

Localized keys are used for content ciphering operations, while master keys
serve as a source for key localization to accommodate new peer SNMP engines.

Normally, the users do not have exposure to either of these keys, however
that may be helpful from debugging and research perspective.

The following table lists master and localized authentication keys for
plain-text key `authkey1` and Security Engine ID
`0x80004fb805636c6f75644dab22cc` (first in the
:ref:`list <simulated-snmp-engines>`).

+----------+----------------------------+----------------------------+
| Protocol | Master key                 | Localized key              |
+----------+----------------------------+----------------------------+
| MD5      | 0x1dcf59e86553b3afa5d32fd5 | 0x6b99c475259ef7976cf8d028 |
|          | d61bf0cf                   | a3381eeb                   |
+----------+----------------------------+----------------------------+
| SHA      | 0xc633ad20156b8459c3aa6149 | 0x14e7b50e65e4e95ac6e44f61 |
|          | 20de69a09064b9a7           | ebcf477dc5611053           |
+----------+----------------------------+----------------------------+
| SHA224   | 0x5466eeba677bbb18b4bfe07f | 0xf2a2ebaa9677ad2862555962 |
|          | ff438a9596fe62cb324c61e20f | 86ca4fb7ec22f52405cb0aac33 |
|          | 0ecb80                     | 4c5f15                     |
+----------+----------------------------+----------------------------+
| SHA256   | 0x09f0d17dd379971adecb56fe | 0x51df668ef9f1d318c9d0dae5 |
|          | e269e22634cb39d44265dc2fe6 | 35fbcca7e99e4d7f93f858679c |
|          | 9b6070eefe7c87             | 98084995efc14a             |
+----------+----------------------------+----------------------------+
| SHA384   | 0x45ab54fe8868afcc9eded0a8 | 0x124867fefad915e22e64fd04 |
|          | 73dd5ee7da5d1835f03d90fcdb | d959512d9d7da219eb441b432a |
|          | 6d9c3ccb683e42f95f16c1b390 | f59da84b766ae9457ff963dfc6 |
|          | 82a55cb2dcdb4fc86f12       | 68d331c1ebb7c6a18b2a       |
+----------+----------------------------+----------------------------+
| SHA512   | 0x76c73c5db5a40284b15f8d52 | 0xc336e5e6396926813d623984 |
|          | a6241521d28303185225f10cc8 | 610e8f0cd7f419da75c82ac509 |
|          | 5020320f5c0458d0caffa3f2c6 | 27c84fd92027f7cdd849ce9830 |
|          | 94f3376b07e3797b943d103e9c | 36dca67bfb1e8fde2a8c2d45cd |
|          | 76b311c1372721e21456a20b16 | 2f0d3e0b0b929f7dda462a58cf |
+----------+----------------------------+----------------------------+

The following table lists master and localized privacy keys for plain-text
key `privkey1` and Security Engine ID `0x80004fb805636c6f75644dab22cc`
(first in the :ref:`list <simulated-snmp-engines>`).

+----------------+------------------------+-------------------------+
| Protocols      | Master key             | Localized key           |
| Privacy(Auth)  |                        |                         |
+----------------+------------------------+-------------------------+
| DES(MD5)       | 0xec5ab55e93e1d85cb684 | 0x92b5ef98f0a216885e73  |
|                | 6d0f23e845e0           | 944e58c07345            |
+----------------+------------------------+-------------------------+
| 3DES(MD5)      | 0xec5ab55e93e1d85cb684 | 0x92b5ef98f0a216885e73  |
|                | 6d0f23e845e0           | 944e58c07345d7319a6d7a  |
|                |                        | 6d174e1adfffad3fb68104  |
+----------------+------------------------+-------------------------+
| AES(MD5)       | 0xec5ab55e93e1d85cb684 | 0x92b5ef98f0a216885e73  |
|                | 6d0f23e845e0           | 944e58c07345            |
+----------------+------------------------+-------------------------+
| AES128(MD5)    | 0xec5ab55e93e1d85cb684 | 0x92b5ef98f0a216885e73  |
|                | 6d0f23e845e0           | 944e58c07345            |
+----------------+------------------------+-------------------------+
| AES192(MD5)    | 0xec5ab55e93e1d85cb684 | 0x92b5ef98f0a216885e73  |
|                | 6d0f23e845e0           | 944e58c07345d7319a6d7a  |
|                |                        | 6d174e                  |
+----------------+------------------------+-------------------------+
| AES256(MD5)    | 0xec5ab55e93e1d85cb684 | 0x92b5ef98f0a216885e73  |
|                | 6d0f23e845e0           | 944e58c07345d7319a6d7a  |
|                |                        | 6d174e1adfffad3fb68104  |
+----------------+------------------------+-------------------------+
| DES(SHA)       | 0x11f1d78c4da05d9ad426 | 0xb36869d8d20f0ca4e44c  |
|                | 90e3af088b923bc16e99   | d9215ba00c0d            |
+----------------+------------------------+-------------------------+
| 3DES(SHA)      | 0x11f1d78c4da05d9ad426 | 0xb36869d8d20f0ca4e44c  |
|                | 90e3af088b923bc16e99   | d9215ba00c0da8bab26db2  |
|                |                        | 24cf77693d461ff5d85041  |
+----------------+------------------------+-------------------------+
| AES(SHA)       | 0x11f1d78c4da05d9ad426 | 0xb36869d8d20f0ca4e44c  |
|                | 90e3af088b923bc16e99   | d9215ba00c0d            |
+----------------+------------------------+-------------------------+
| AES128(SHA)    | 0x11f1d78c4da05d9ad426 | 0xb36869d8d20f0ca4e44c  |
|                | 90e3af088b923bc16e99   | d9215ba00c0d            |
+----------------+------------------------+-------------------------+
| AES192(SHA)    | 0x11f1d78c4da05d9ad426 | 0xb36869d8d20f0ca4e44c  |
|                | 90e3af088b923bc16e99   | d9215ba00c0da8bab26db2  |
|                |                        | 24cf77                  |
+----------------+------------------------+-------------------------+
| AES256(SHA)    | 0x11f1d78c4da05d9ad426 | 0xb36869d8d20f0ca4e44c  |
|                | 90e3af088b923bc16e99   | d9215ba00c0da8bab26db2  |
|                |                        | 24cf77693d461ff5d85041  |
+----------------+------------------------+-------------------------+
| DES(SHA224)    | 0xaaba93638e15f9e7db50 | 0x93e91004d964dc3dc28c  |
|                | 6f08c9313d5da8125d8793 | 30606db75649            |
|                | 1b87c490d3fd39         |                         |
+----------------+------------------------+-------------------------+
| 3DES(SHA224)   | 0xaaba93638e15f9e7db50 | 0x93e91004d964dc3dc28c  |
|                | 6f08c9313d5da8125d8793 | 30606db75649c6846214a5  |
|                | 1b87c490d3fd39         | b4a12ded61da56d416df09  |
+----------------+------------------------+-------------------------+
| AES(SHA224)    | 0xaaba93638e15f9e7db50 | 0x93e91004d964dc3dc28c  |
|                | 6f08c9313d5da8125d8793 | 30606db75649            |
|                | 1b87c490d3fd39         |                         |
+----------------+------------------------+-------------------------+
| AES128(SHA224) | 0xaaba93638e15f9e7db50 | 0x93e91004d964dc3dc28c  |
|                | 6f08c9313d5da8125d8793 | 30606db75649            |
|                | 1b87c490d3fd39         |                         |
+----------------+------------------------+-------------------------+
| AES192(SHA224) | 0xaaba93638e15f9e7db50 | 0x93e91004d964dc3dc28c  |
|                | 6f08c9313d5da8125d8793 | 30606db75649c6846214a5  |
|                | 1b87c490d3fd39         | b4a12d                  |
+----------------+------------------------+-------------------------+
| AES256(SHA224) | 0xaaba93638e15f9e7db50 | 0x93e91004d964dc3dc28c  |
|                | 6f08c9313d5da8125d8793 | 30606db75649c6846214a5  |
|                | 1b87c490d3fd39         | b4a12ded61da56d416df09  |
+----------------+------------------------+-------------------------+
| DES(SHA256)    | 0x4f2e0e74847cd65fb8f1 | 0x505a4df14810f18c11f5  |
|                | 2c1f101c65ef6afd60885e | 2b4cac8fe860            |
|                | f18af6fc011245a33aeca7 |                         |
+----------------+------------------------+-------------------------+
| 3DES(SHA256)   | 0x4f2e0e74847cd65fb8f1 | 0x505a4df14810f18c11f5  |
|                | 2c1f101c65ef6afd60885e | 2b4cac8fe8604426cfcfc4  |
|                | f18af6fc011245a33aeca7 | 5b41556e2bf9e3a668f2fe  |
+----------------+------------------------+-------------------------+
| AES(SHA256)    | 0x4f2e0e74847cd65fb8f1 | 0x505a4df14810f18c11f5  |
|                | 2c1f101c65ef6afd60885e | 2b4cac8fe860            |
|                | f18af6fc011245a33aeca7 |                         |
+----------------+------------------------+-------------------------+
| AES128(SHA256) | 0x4f2e0e74847cd65fb8f1 | 0x505a4df14810f18c11f52 |
|                | 2c1f101c65ef6afd60885e | b4cac8fe860             |
|                | f18af6fc011245a33aeca7 |                         |
+----------------+------------------------+-------------------------+
| AES192(SHA256) | 0x4f2e0e74847cd65fb8f1 | 0x505a4df14810f18c11f52 |
|                | 2c1f101c65ef6afd60885e | b4cac8fe8604426cfcfc45b |
|                | f18af6fc011245a33aeca7 | 4155                    |
+----------------+------------------------+-------------------------+
| AES256(SHA256) | 0x4f2e0e74847cd65fb8f1 | 0x505a4df14810f18c11f52 |
|                | 2c1f101c65ef6afd60885e | b4cac8fe8604426cfcfc45b |
|                | f18af6fc011245a33aeca7 | 41556e2bf9e3a668f2fe    |
+----------------+------------------------+-------------------------+
| DES(SHA384)    | 0x81dd5e2a020f424ed6d9 | 0xf2bdc0d6770e1e60f28cb |
|                | 62b5ada3ae82c8bc9871a3 | d5970d50cd8             |
|                | 84cb2dca0007dd465f9932 |                         |
|                | 350ac307caabf4103513d0 |                         |
|                | 7275d50a9a             |                         |
+----------------+------------------------+-------------------------+
| 3DES(SHA384)   | 0x81dd5e2a020f424ed6d9 | 0xf2bdc0d6770e1e60f28cb |
|                | 62b5ada3ae82c8bc9871a3 | d5970d50cd85c71d2e53512 |
|                | 84cb2dca0007dd465f9932 | 427ca2db4f32971452a1    |
|                | 350ac307caabf4103513d0 |                         |
|                | 7275d50a9a             |                         |
+----------------+------------------------+-------------------------+
| AES(SHA384)    | 0x81dd5e2a020f424ed6d9 | 0xf2bdc0d6770e1e60f28cb |
|                | 62b5ada3ae82c8bc9871a3 | d5970d50cd8             |
|                | 84cb2dca0007dd465f9932 |                         |
|                | 350ac307caabf4103513d0 |                         |
|                | 7275d50a9a             |                         |
+----------------+------------------------+-------------------------+
| AES128(SHA384) | 0x81dd5e2a020f424ed6d9 | 0xf2bdc0d6770e1e60f28cb |
|                | 62b5ada3ae82c8bc9871a3 | d5970d50cd8             |
|                | 84cb2dca0007dd465f9932 |                         |
|                | 350ac307caabf4103513d0 |                         |
|                | 7275d50a9a             |                         |
+----------------+------------------------+-------------------------+
| AES192(SHA384) | 0x81dd5e2a020f424ed6d9 | 0xf2bdc0d6770e1e60f28cb |
|                | 62b5ada3ae82c8bc9871a3 | d5970d50cd85c71d2e53512 |
|                | 84cb2dca0007dd465f9932 | 427c                    |
|                | 350ac307caabf4103513d0 |                         |
|                | 7275d50a9a             |                         |
+----------------+------------------------+-------------------------+
| AES256(SHA384) | 0x81dd5e2a020f424ed6d9 | 0xf2bdc0d6770e1e60f28cb |
|                | 62b5ada3ae82c8bc9871a3 | d5970d50cd85c71d2e53512 |
|                | 84cb2dca0007dd465f9932 | 427ca2db4f32971452a1    |
|                | 350ac307caabf4103513d0 |                         |
|                | 7275d50a9a             |                         |
+----------------+------------------------+-------------------------+
| DES(SHA512)    | 0x7af2b74ffb38cce78585 | 0x3c8a3d93e2913b94e61b2 |
|                | 6185c7c1e1263201d6f325 | 11a67b9e385             |
|                | 48272e7d5638ffb15160ab |                         |
|                | 1191ce74da297ffb833931 |                         |
|                | 84b30867dad1642444dbd7 |                         |
|                | 06359b5e68ff71d7d079   |                         |
+----------------+------------------------+-------------------------+
| 3DES(SHA512)   | 0x7af2b74ffb38cce78585 | 0x3c8a3d93e2913b94e61b2 |
|                | 6185c7c1e1263201d6f325 | 11a67b9e38586e533f02f88 |
|                | 48272e7d5638ffb15160ab | 4df6e5b04271d71e118d    |
|                | 1191ce74da297ffb833931 |                         |
|                | 84b30867dad1642444dbd7 |                         |
|                | 06359b5e68ff71d7d079   |                         |
+----------------+------------------------+-------------------------+
| AES(SHA512)    | 0x7af2b74ffb38cce78585 | 0x3c8a3d93e2913b94e61b2 |
|                | 6185c7c1e1263201d6f325 | 11a67b9e385             |
|                | 48272e7d5638ffb15160ab |                         |
|                | 1191ce74da297ffb833931 |                         |
|                | 84b30867dad1642444dbd7 |                         |
|                | 06359b5e68ff71d7d079   |                         |
+----------------+------------------------+-------------------------+
| AES128(SHA512) | 0x7af2b74ffb38cce78585 | 0x3c8a3d93e2913b94e61b2 |
|                | 6185c7c1e1263201d6f325 | 11a67b9e385             |
|                | 48272e7d5638ffb15160ab |                         |
|                | 1191ce74da297ffb833931 |                         |
|                | 84b30867dad1642444dbd7 |                         |
|                | 06359b5e68ff71d7d079   |                         |
+----------------+------------------------+-------------------------+
| AES192(SHA512) | 0x7af2b74ffb38cce78585 | 0x3c8a3d93e2913b94e61b2 |
|                | 6185c7c1e1263201d6f325 | 11a67b9e38586e533f02f88 |
|                | 48272e7d5638ffb15160ab | 4df6                    |
|                | 1191ce74da297ffb833931 |                         |
|                | 84b30867dad1642444dbd7 |                         |
|                | 06359b5e68ff71d7d079   |                         |
+----------------+------------------------+-------------------------+
| AES256(SHA512) | 0x7af2b74ffb38cce78585 | 0x3c8a3d93e2913b94e61b2 |
|                | 6185c7c1e1263201d6f325 | 11a67b9e38586e533f02f88 |
|                | 48272e7d5638ffb15160ab | 4df6e5b04271d71e118d    |
|                | 1191ce74da297ffb833931 |                         |
|                | 84b30867dad1642444dbd7 |                         |
|                | 06359b5e68ff71d7d079   |                         |
+----------------+------------------------+-------------------------+

.. note::

   Master and localized privacy (encryption) keys also depend on authentication
   protocol.

.. _simulated-data:

Simulation data
---------------

Each of the :ref:`SNMP engines <simulated-snmp-engines>` simulate multiple SNMP agents addressable
by the following SNMP query parameters:

+--------------------------------------------------------------------+------------------------------------+------------------------------------+
| **SNMP agent**                                                     | **SNMP community**                 | **SNMP context name**              |
+--------------------------------------------------------------------+------------------------------------+------------------------------------+
| Dynamically variated, writable SNMP Agent                          | public                             | <empty>                            |
+--------------------------------------------------------------------+------------------------------------+------------------------------------+
| Static snapshot of a Linux host                                    | recorded/linux-full-walk           | a172334d7d97871b72241397f713fa12   |
+--------------------------------------------------------------------+------------------------------------+------------------------------------+
| Static snapshot of a Windows XP PC                                 | foreignformats/winxp2              | da761cfc8c94d3aceef4f60f049105ba   |
+--------------------------------------------------------------------+------------------------------------+------------------------------------+
| Series of static snapshots of live IF-MIB::interfaces              | variation/multiplex                | 1016117d6836664ee15b9b2af5642c3c   |
+--------------------------------------------------------------------+------------------------------------+------------------------------------+
| Simulated IF-MIB::interfaces table with ever increasing counters   | variation/virtualtable             | 329a935947144eb87ad0cdc5e08927b1   |
+--------------------------------------------------------------------+------------------------------------+------------------------------------+

TRAP sink
---------

Besides simulated SNMP Agents we are also running a multilingual
SNMP Notification Receiver. It will consume and optionally acknowledge
SNMP TRAP/INFORM messages you might send to *demo.snmplabs.com:162*.

SNMPv1/v2c community name is **public**. Configured SNMPv3 USM users
and keys are :ref:`the same <simulated-usm-users>` as for SNMP agents.

Keep in mind that our SNMPv3 TRAP receiving service is configured for
authoritative SNMP engine ID **8000000001020304**. You would have to
explicitly configure it to your SNMP notification originator.

Obviously, you won't get any response from your TRAP messages, however
you will get an acknowledgement for the INFORM packets you send us.

Examples
--------

Variated table walk
+++++++++++++++++++

To query simulated live `IF-MIB::interfaces <http://mibs.snmplabs.com/asn1/IF-MIB>`_ over
SNMPv2c use the following command:

.. code-block:: bash

    $ snmpwalk -v2c -c variation/virtualtable \
        demo.snmplabs.com IF-MIB::interfaces

Modify managed objects
++++++++++++++++++++++

Some of the simulated objects are configured writable so you can experiment
with SNMP SET:

.. code-block:: bash

    $ snmpwalk -v2c -c public demo.snmplabs.com system
    ...
    SNMPv2-MIB::sysORDescr.1 = STRING: Please modify me
    SNMPv2-MIB::sysORUpTime.1 = Timeticks: (1) 0:00:00.01
    $
    $ snmpset -v2c -c private demo.snmplabs.com \
      SNMPv2-MIB::sysORDescr.1 = 'Here is my new note'
    SNMPv2-MIB::sysORDescr.1 = STRING: Here is my new note
    $ snmpset -v2c -c private demo.snmplabs.com \
      SNMPv2-MIB::sysORUpTime.1 = 321
    SNMPv2-MIB::sysORUpTime.1 = Timeticks: (321) 0:00:03.21
    $ snmpwalk -v2c -c public demo.snmplabs.com system
    ...
    SNMPv2-MIB::sysORDescr.1 = STRING: Here is my new note
    SNMPv2-MIB::sysORUpTime.1 = Timeticks: (321) 0:00:03.21

Discover agents
+++++++++++++++

The above table is not complete, you could always figure out the most
actual list of simulated SNMP Agents by fetching relevant SNMP table
off the SNMP Simulator:

.. code-block:: bash

    $ snmpwalk -v2c -c index demo.snmplabs.com 1.3.6
    SNMPv2-SMI::enterprises.20408.999.1.1.1 = STRING: "/usr/snmpsim/data/1.3.6.1.6.1.1.0/127.0.0.1.snmprec"
    SNMPv2-SMI::enterprises.20408.999.1.1.2 = STRING: "/usr/snmpsim/data/public.snmprec"
    SNMPv2-SMI::enterprises.20408.999.1.1.3 = STRING: "/usr/snmpsim/data/foreignformats/winxp2.sapwalk"
    ...

SNMPv3 commands
+++++++++++++++

SNMPv3 command example using `MD5` protocol for authentication, `DES` for
privacy and plain-text keys:

.. code-block:: bash

   $ snmpget -v3 -l authPriv \
       -u usr-md5-des \
       -a md5 -A authkey1 \
       -x des -X privkey1 \
       demo.snmplabs.com sysDescr.0
   SNMPv2-MIB::sysDescr.0 = STRING: Linux zeus 4.8.6.5-smp #2 SMP Sun Nov 13 14:58:11 CDT 2016 i686

SNMPv3 command example using `MD5` protocol for authentication, `DES` for
privacy and master keys:

.. code-block:: bash

   $ snmpget -v3 -l authPriv \
       -u usr-md5-des \
       -a md5 -3m 0x1dcf59e86553b3afa5d32fd5d61bf0cf \
       -x des -3M 0xec5ab55e93e1d85cb6846d0f23e845e0 \
       demo.snmplabs.com sysDescr.0
    SNMPv2-MIB::sysDescr.0 = STRING: Linux zeus 4.8.6.5-smp #2 SMP Sun Nov 13 14:58:11 CDT 2016 i686

SNMPv3 command example using `MD5` protocol for authentication, `DES` for
privacy and localized keys:

.. code-block:: bash

   $ snmpget -v3 -l authPriv \
       -u usr-md5-des \
       -e 0x80004fb805636c6f75644dab22cc \
       -a md5 -3k 0x6b99c475259ef7976cf8d028a3381eeb \
       -x des -3K 0x92b5ef98f0a216885e73944e58c07345 \
       demo.snmplabs.com sysDescr.0
    SNMPv2-MIB::sysDescr.0 = STRING: Linux zeus 4.8.6.5-smp #2 SMP Sun Nov 13 14:58:11 CDT 2016 i686

.. note::

   Technically, for localized keys to be found in the local database, SNMP
   security engine ID should be given as a hint. However, Net-SNMP tools
   seem to have some fuzziness inside that makes them finding localized
   keys even without `-e` option.

SNMPv3 notifications
++++++++++++++++++++

Example SNMPv3 TRAP would look like this:

.. code-block:: bash

    $ snmptrap -v3 -l authPriv \
        -u usr-md5-des \
        -e 8000000001020304 \
        -a md5 -A authkey1 \
        -x des -X privkey1 \
        demo.snmplabs.com \
        12345 1.3.6.1.4.1.20408.4.1.1.2 1.3.6.1.2.1.1.1.0 s hello

Normal SNMP engine ID discovery would work for SNMP INFORMs, hence
securityEngineId should not be used:

.. code-block:: bash

    $ snmpinform -v3 -l authPriv \
        -u usr-md5-des \
        -a md5 -A authkey1 \
        -x des -X privkey1 \
        demo.snmplabs.com 12345 \
        1.3.6.1.4.1.20408.4.1.1.2 1.3.6.1.2.1.1.1.0 s hello
