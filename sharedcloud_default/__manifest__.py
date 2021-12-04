##############################################################################
#
#    Copyright (C) 2021  Quilsoft  (http://www.quilsoft.com)
#    All Rights Reserved.
#
##############################################################################

{
    'name': 'sharedcloud',
    'version': '12.0.1.0.0',
    'category': 'Tools',
    'summary': "Proyect module for SHared Cloud",
    'author': "Crumges",
    'website': 'crumges.com',
    'license': 'AGPL-3',
    'depends': [
            # Modulos odoo
            'sale',
            'purchase',
            'stock',
            'sale_management',
            'account',
            'purchase',
            'point_of_sale',

        ],
    'installable': True,

    'env-ver': '2',
    'odoo-license': 'CE',
    'config': [

        # 'addons_path' is always computed looking for the repositories in sources
        # 'data_dir' is a fixed location inside docker odoo image

        # You should use 2 worker threads + 1 cron thread per available CPU,
        # and 1 CPU per 10 concurent users.
        # if ommited oe will calculate workers and cron´s based on # of cpu
        #        'workers = 0',
                'max_cron_threads = 1',

        # Number of requests a worker will process before being recycled and
        # restarted. Defaults to 8192 if ommited
                'limit_request = 8192',

        # Maximum allowed virtual memory per worker. If the limit is exceeded,
        # the worker is killed and recycled at the end of the current request.
        # Defaults to 640MB
                'limit_memory_soft = 2147483648',

        # Hard limit on virtual memory, any worker exceeding the limit will be
        # immediately killed without waiting for the end of the current request
        # processing. Defaults to 768MB.
                'limit_memory_hard = 2684354560',
    ],

    'port': '8069',

    'git-repos': [
        'https://github.com/jobiols/cl-sharedcloud.git -b 12.0 --depth 1',

        # Quilsoft
        #'git@github.com:quilsoft-org/cocacola.git -b main',

        # OCA
        'https://github.com/OCA/account-analytic OCA-account-analytic --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/account-closing OCA-account-closing --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/account-financial-reporting OCA-account-financial-reporting --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/account-financial-tools OCA-account-financial-tools --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/account-invoice-reporting OCA-account-invoice-reporting --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/account-invoicing OCA-account-invoicing --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/account-payment OCA-account-payment --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/account-reconcile OCA-account-reconcile --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/bank-payment OCA-bank-payment --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/business-requirement OCA-business-requirement --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/commission OCA-commission --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/contract OCA-contract --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/credit-control OCA-credit-control --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/crm OCA-crm --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/currency OCA-currency --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/ddmrp OCA-ddmrp --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/delivery-carrier OCA-delivery-carrier --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/dms OCA-dms --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/e-commerce OCA-e-commerce --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/edi OCA-edi --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/event OCA-event --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/field-service OCA-field-service --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/fleet OCA-fleet --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/geospatial OCA-geospatial --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/helpdesk OCA-helpdesk --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/hr OCA-hr --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/knowledge OCA-knowledge --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/maintenance OCA-maintenance --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/management-system OCA-management-system --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/manufacture OCA-manufacture --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/manufacture-reporting OCA-manufacture-reporting --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/margin-analysis OCA-margin-analysis --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/mis-builder OCA-mis-builder --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/multi-company OCA-multi-company --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/oca-custom OCA-oca-custom --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/partner-contact OCA-partner-contact --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/pos OCA-pos --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/product-attribute OCA-product-attribute --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/product-variant OCA-product-variant --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/project OCA-project --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/purchase-reporting OCA-purchase-reporting --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/purchase-workflow OCA-purchase-workflow --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/queue OCA-queue --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/report-print-send OCA-report-print-send --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/reporting-engine OCA-reporting-engine --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/rma OCA-rma --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/sale-reporting OCA-sale-reporting --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/sale-workflow OCA-sale-workflow --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/server-auth OCA-server-auth --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/server-backend OCA-server-backend --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/server-brand OCA-server-brand --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/server-env OCA-server-env --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/server-tools OCA-server-tools --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/server-ux OCA-server-ux --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/social OCA-social --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/stock-logistics-barcode OCA-stock-logistics-barcode --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/stock-logistics-reporting OCA-stock-logistics-reporting --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/stock-logistics-transport OCA-stock-logistics-transport --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/stock-logistics-warehouse OCA-stock-logistics-warehouse --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/stock-logistics-workflow OCA-stock-logistics-workflow --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/survey OCA-survey --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/timesheet OCA-timesheet --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/vertical-association OCA-vertical-association --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/web OCA-web --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/website OCA-website --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/wms OCA-wms --depth 1 --branch 12.0  --single-branch',
        'https://github.com/OCA/management-system OCA-management-system --depth 1 --branch 12.0  --single-branch',

        # Adhoc
        'https://github.com/ingadhoc/account-financial-tools ingadhoc-account-financial-tools --depth 1 --branch 12.0  --single-branch',
        'https://github.com/ingadhoc/account-invoicing ingadhoc-account-invoicing --depth 1 --branch 12.0  --single-branch',
        'https://github.com/ingadhoc/account-payment ingadhoc-account-payment --depth 1 --branch 12.0  --single-branch',
        'https://github.com/ingadhoc/argentina-reporting ingadhoc-argentina-reporting --depth 1 --branch 12.0  --single-branch',
        'https://github.com/ingadhoc/aeroo_reports ingadhoc-aeroo_reports --depth 1 --branch 12.0  --single-branch',
        'https://github.com/ingadhoc/reporting-engine ingadhoc-reporting-engine --depth 1 --branch 12.0  --single-branch', 
        'https://github.com/ingadhoc/argentina-sale ingadhoc-argentina-sale --depth 1 --branch 12.0  --single-branch',
        'https://github.com/ingadhoc/hr ingadhoc-hr --depth 1 --branch 12.0  --single-branch',
        'https://github.com/ingadhoc/miscellaneous ingadhoc-miscellaneous --depth 1 --branch 12.0  --single-branch',
        'https://github.com/ingadhoc/multi-company ingadhoc-multi-company --depth 1 --branch 12.0  --single-branch',
        'https://github.com/ingadhoc/multi-store ingadhoc-multi-store --depth 1 --branch 12.0  --single-branch',
        'https://github.com/ingadhoc/odoo-argentina ingadhoc-odoo-argentina --depth 1 --branch 12.0  --single-branch',
        'https://github.com/ingadhoc/partner ingadhoc-partner --depth 1 --branch 12.0  --single-branch',
        'https://github.com/ingadhoc/product ingadhoc-product --depth 1 --branch 12.0  --single-branch',
        'https://github.com/ingadhoc/project ingadhoc-project --depth 1 --branch 12.0  --single-branch',
        'https://github.com/ingadhoc/purchase ingadhoc-purchase --depth 1 --branch 12.0  --single-branch',
        'https://github.com/ingadhoc/sale ingadhoc-sale --depth 1 --branch 12.0  --single-branch',
        'https://github.com/ingadhoc/stock ingadhoc-stock --depth 1 --branch 12.0  --single-branch',
        'https://github.com/ingadhoc/website ingadhoc-website --depth 1 --branch 12.0  --single-branch',
        'https://github.com/ingadhoc/account-financial-tools.git --depth 1 --branch 12.0  --single-branch',
        'https://github.com/ingadhoc/patches ingadhoc-patches --depth 1 --branch 12.0  --single-branch'

        # Regaby
        'https://github.com/regaby/odoo-custom.git regaby-odoo-custom --depth 1 --branch 12.0  --single-branch'
    ],

    # list of images to use in the form 'name image-url'
    'docker-images': [
        'odoo jobiols/odoo-jeo:12.0',
        'postgres postgres:10.1-alpine',
    ]
}
