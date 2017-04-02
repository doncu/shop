#!/usr/bin/env python


if __name__ == '__main__':
    import sys
    '.' not in sys.path and sys.path.insert(0, '.')

    from shop import db
    db.import_all()
    db.Base.metadata.create_all(db.engine)
