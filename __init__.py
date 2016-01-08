# Will give:
# ValueError: Attempted relative import in non-package

# To prevent this error:
# 1. import jpg
#    import png
# 2. From the parent directory
#    python -m rel_import.__init__

from . import jpg
from . import png


if __name__ == "__main__":
    print "test"
