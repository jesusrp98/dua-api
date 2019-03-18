import hug

import internal

router = hug.route.API(__name__)
router.get('/grados')(internal.root)
router.get('/notas')(internal.root)
