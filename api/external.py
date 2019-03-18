import hug

import notas

router = hug.route.API(__name__)
router.get('/notas')(notas.root)
