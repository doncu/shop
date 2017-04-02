#!/usr/bin/env python


if __name__ == '__main__':
    import sys
    '.' not in sys.path and sys.path.insert(0, '.')

    from shop.db import import_all
    from shop.db import Base
    import_all()
    Base.metadata.create_all()
