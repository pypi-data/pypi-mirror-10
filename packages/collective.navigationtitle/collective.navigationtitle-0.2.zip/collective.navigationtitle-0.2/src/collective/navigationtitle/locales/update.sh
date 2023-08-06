#! /bin/sh
#
# to add/update your translation
# add the corresponding lang folder structure and rerun this script
#
# i18ndude should be available in current $PATH (eg by running
# ``export PATH=$PATH:$BUILDOUT_DIR/bin`` when i18ndude is located in your buildout's bin directory)

domain="collective.navigationtitle"
i18ndude rebuild-pot --pot ${domain}.pot --create ${domain} ../
i18ndude sync --pot ${domain}.pot */LC_MESSAGES/${domain}.po

i18ndude sync --pot plone-manual.pot */LC_MESSAGES/plone.po