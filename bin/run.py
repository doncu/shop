import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Run Clstream')

    parser.add_argument(
        '--host',
        # default='0.0.0.0',
        default='127.0.0.1',
        help='Host for run'
    )

    parser.add_argument(
        '--port',
        default=5000,
        type=int,
        help='Host for run'
    )

    parser.add_argument(
        '--no-debug',
        dest='debug',
        action='store_false',
        default=True
    )

    args = parser.parse_args()

    import sys

    '.' not in sys.path and sys.path.insert(0, '.')

    from shop.app import app

    app.run(debug=args.debug, port=args.port, host=args.host, threaded=True)
