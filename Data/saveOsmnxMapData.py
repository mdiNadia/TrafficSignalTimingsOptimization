import osmnx as ox

place_name = "Tehran, Iran"
# دانلود شبکه جاده‌ای
graph = ox.graph_from_place(place_name, network_type='drive')
# ذخیره کردن شبکه جاده‌ای به صورت فایل GraphML
ox.save_graphml(graph, filepath='Data/Tehran_drive.graphml')
