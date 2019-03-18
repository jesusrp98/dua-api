import hug

import internal

router = hug.route.API(__name__)
router.get('/home')(internal.root)
