.. -*- coding: utf-8 -*-

==========
storagedef
==========

Abstract storage layer


Install
=======

from PyPI::

  pip install storagedef


from Source::

  pip install -e .


How to use
==========

If you use ``pyramid``::

  import storagedef

  def main(global_config, **settings):
      storage_session = storagedef.Session.from_config(settings, prefix='mystorage.')
      config = Configurator(settings=settings)

      # Some your configuration using storage_session

      return config.make_wsgi_app()


Configuration Keys
==================

Example ini-file if you use 'mystorage.' as prefix::

  mystorage.engine = storagedef.engines.s3:S3StorageEngine
  mystorage.credentials_file = ~/.aws/credentials
  mystorage.config_file = ~/.aws/config
  mystorage.region = ap-northeast-1
  mystorage.bucket = some-test-bucket
  mystorage.acl = public-read

another ini-file using localmem::

  mystorage.engine = storagedef.engines.localmemory:LocalMemoryStorageEngine
