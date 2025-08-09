{
    "name": "Finanzas Avanzadas",
    "version": "18.0.1.0.0",
    "author": "solbank1",
    "license": "LGPL-3",
    "depends": ["base"],
    "application": True,        # ← importante para que salga como app
    "installable": True,
    "category": "Accounting",   # alguna categoría válida
    "data": [
        "security/ir.model.access.csv",
        "views/menu_views.xml",
    ],
}

