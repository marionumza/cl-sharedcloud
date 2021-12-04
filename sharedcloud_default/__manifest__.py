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
        'https://github.com/OCA/account-analytic OCA-account-analytic -b 12.0',
        'https://github.com/OCA/account-closing OCA-account-closing -b 12.0',
        'https://github.com/OCA/account-financial-reporting OCA-account-financial-reporting -b 12.0',
        'https://github.com/OCA/account-financial-tools OCA-account-financial-tools -b 12.0',
        'https://github.com/OCA/account-invoice-reporting OCA-account-invoice-reporting -b 12.0',
        'https://github.com/OCA/account-invoicing OCA-account-invoicing -b 12.0',
        'https://github.com/OCA/account-payment OCA-account-payment -b 12.0',
        'https://github.com/OCA/account-reconcile OCA-account-reconcile -b 12.0',
        'https://github.com/OCA/bank-payment OCA-bank-payment -b 12.0',
        'https://github.com/OCA/business-requirement OCA-business-requirement -b 12.0',
        'https://github.com/OCA/commission OCA-commission -b 12.0',
        'https://github.com/OCA/contract OCA-contract -b 12.0',
        'https://github.com/OCA/credit-control OCA-credit-control -b 12.0',
        'https://github.com/OCA/crm OCA-crm -b 12.0',
        'https://github.com/OCA/currency OCA-currency -b 12.0',
        'https://github.com/OCA/ddmrp OCA-ddmrp -b 12.0',
        'https://github.com/OCA/delivery-carrier OCA-delivery-carrier -b 12.0',
        'https://github.com/OCA/dms OCA-dms -b 12.0',
        'https://github.com/OCA/e-commerce OCA-e-commerce -b 12.0',
        'https://github.com/OCA/edi OCA-edi -b 12.0',
        'https://github.com/OCA/event OCA-event -b 12.0',
        'https://github.com/OCA/field-service OCA-field-service -b 12.0',
        'https://github.com/OCA/fleet OCA-fleet -b 12.0',
        'https://github.com/OCA/geospatial OCA-geospatial -b 12.0',
        'https://github.com/OCA/helpdesk OCA-helpdesk -b 12.0',
        'https://github.com/OCA/hr OCA-hr -b 12.0',
        'https://github.com/OCA/knowledge OCA-knowledge -b 12.0',
        'https://github.com/OCA/maintenance OCA-maintenance -b 12.0',
        'https://github.com/OCA/management-system OCA-management-system -b 12.0',
        'https://github.com/OCA/manufacture OCA-manufacture -b 12.0',
        'https://github.com/OCA/manufacture-reporting OCA-manufacture-reporting -b 12.0',
        'https://github.com/OCA/margin-analysis OCA-margin-analysis -b 12.0',
        'https://github.com/OCA/mis-builder OCA-mis-builder -b 12.0',
        'https://github.com/OCA/multi-company OCA-multi-company -b 12.0',
        'https://github.com/OCA/oca-custom OCA-oca-custom -b 12.0',
        'https://github.com/OCA/partner-contact OCA-partner-contact -b 12.0',
        'https://github.com/OCA/pos OCA-pos -b 12.0',
        'https://github.com/OCA/product-attribute OCA-product-attribute -b 12.0',
        'https://github.com/OCA/product-variant OCA-product-variant -b 12.0',
        'https://github.com/OCA/project OCA-project -b 12.0',
        'https://github.com/OCA/purchase-reporting OCA-purchase-reporting -b 12.0',
        'https://github.com/OCA/purchase-workflow OCA-purchase-workflow -b 12.0',
        'https://github.com/OCA/queue OCA-queue -b 12.0',
        'https://github.com/OCA/report-print-send OCA-report-print-send -b 12.0',
        'https://github.com/OCA/reporting-engine OCA-reporting-engine -b 12.0',
        'https://github.com/OCA/rma OCA-rma -b 12.0',
        'https://github.com/OCA/sale-reporting OCA-sale-reporting -b 12.0',
        'https://github.com/OCA/sale-workflow OCA-sale-workflow -b 12.0',
        'https://github.com/OCA/server-auth OCA-server-auth -b 12.0',
        'https://github.com/OCA/server-backend OCA-server-backend -b 12.0',
        'https://github.com/OCA/server-brand OCA-server-brand -b 12.0',
        'https://github.com/OCA/server-env OCA-server-env -b 12.0',
        'https://github.com/OCA/server-tools OCA-server-tools -b 12.0',
        'https://github.com/OCA/server-ux OCA-server-ux -b 12.0',
        'https://github.com/OCA/social OCA-social -b 12.0',
        'https://github.com/OCA/stock-logistics-barcode OCA-stock-logistics-barcode -b 12.0',
        'https://github.com/OCA/stock-logistics-reporting OCA-stock-logistics-reporting -b 12.0',
        'https://github.com/OCA/stock-logistics-transport OCA-stock-logistics-transport -b 12.0',
        'https://github.com/OCA/stock-logistics-warehouse OCA-stock-logistics-warehouse -b 12.0',
        'https://github.com/OCA/stock-logistics-workflow OCA-stock-logistics-workflow -b 12.0',
        'https://github.com/OCA/survey OCA-survey -b 12.0',
        'https://github.com/OCA/timesheet OCA-timesheet -b 12.0',
        'https://github.com/OCA/vertical-association OCA-vertical-association -b 12.0',
        'https://github.com/OCA/web OCA-web -b 12.0',
        'https://github.com/OCA/website OCA-website -b 12.0',
        'https://github.com/OCA/wms OCA-wms -b 12.0',
        'https://github.com/OCA/management-system OCA-management-system -b 12.0',

        # Adhoc
        'https://github.com/ingadhoc/account-financial-tools ingadhoc-account-financial-tools -b 12.0',
        'https://github.com/ingadhoc/account-invoicing ingadhoc-account-invoicing -b 12.0',
        'https://github.com/ingadhoc/account-payment ingadhoc-account-payment -b 12.0',
        'https://github.com/ingadhoc/argentina-reporting ingadhoc-argentina-reporting -b 12.0',
        'https://github.com/ingadhoc/aeroo_reports ingadhoc-aeroo_reports -b 12.0',
        'https://github.com/ingadhoc/reporting-engine ingadhoc-reporting-engine -b 12.0', 
        'https://github.com/ingadhoc/argentina-sale ingadhoc-argentina-sale -b 12.0',
        'https://github.com/ingadhoc/hr ingadhoc-hr -b 12.0',
        'https://github.com/ingadhoc/miscellaneous ingadhoc-miscellaneous -b 12.0',
        'https://github.com/ingadhoc/multi-company ingadhoc-multi-company -b 12.0',
        'https://github.com/ingadhoc/multi-store ingadhoc-multi-store -b 12.0',
        'https://github.com/ingadhoc/odoo-argentina ingadhoc-odoo-argentina -b 12.0',
        'https://github.com/ingadhoc/partner ingadhoc-partner -b 12.0',
        'https://github.com/ingadhoc/product ingadhoc-product -b 12.0',
        'https://github.com/ingadhoc/project ingadhoc-project -b 12.0',
        'https://github.com/ingadhoc/purchase ingadhoc-purchase -b 12.0',
        'https://github.com/ingadhoc/sale ingadhoc-sale -b 12.0',
        'https://github.com/ingadhoc/stock ingadhoc-stock -b 12.0',
        'https://github.com/ingadhoc/website ingadhoc-website -b 12.0',
        'https://github.com/ingadhoc/account-financial-tools.git -b 12.0',
        'https://github.com/ingadhoc/patches ingadhoc-patches -b 12.0'

        # Regaby
        'https://github.com/regaby/odoo-custom.git regaby-odoo-custom -b 12.0'
    ],

    # list of images to use in the form 'name image-url'
    'docker-images': [
        'odoo jobiols/odoo-jeo:12.0',
        'postgres postgres:10.1-alpine',
    ]
}
