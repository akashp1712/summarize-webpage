def fetch_base_url(cfg=None):
    base_url = ''
    if cfg is not None and cfg.has_section('backend'):
        base_url = cfg.get('backend', 'base_url') if cfg.has_option('backend', 'base_url') else ''

    return base_url
