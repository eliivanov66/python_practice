import html_creater as hc
import xml_creater as xc
import data_provider as dp

# 1
# print(hc.html_create())
# print(xc.xml_create())

# 2
hc.html_collection_create(xc.xml_collection_create(dp.data_collector()))

