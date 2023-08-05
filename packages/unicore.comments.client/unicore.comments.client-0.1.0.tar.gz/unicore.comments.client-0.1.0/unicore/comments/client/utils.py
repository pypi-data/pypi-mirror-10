def client_from_config(
        client_cls, configuration, prefix='unicorecomments.', **kwargs):
    settings = dict((key[len(prefix):], value)
                    for key, value in configuration.iteritems()
                    if key.startswith(prefix))
    settings.update(kwargs)
    return client_cls(**settings)
