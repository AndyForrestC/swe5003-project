# import pyspark.sql.types as T

BOOTSTRAP_SERVERS = 'kafka:29092'
TOPIC = 'supply_chain_data'
# STREAM_SCHEMA = T.StructType([
#     T.StructField("Type", T.StringType()),
#     T.StructField("Days_for_shipping_real", T.FloatType()),
#     T.StructField("Days_for_shipment_scheduled", T.FloatType()),
#     T.StructField("Benefit_per_order", T.FloatType()),
#     T.StructField("Sales_per_customer", T.FloatType()),
#     T.StructField("Delivery_Status", T.StringType()),
#     T.StructField("Late_delivery_risk", T.IntegerType()),
#     T.StructField("Category_Id", T.IntegerType()),
#     T.StructField("Category_Name", T.StringType()),
#     T.StructField("Customer_City", T.StringType()),
#     T.StructField("Customer_Country", T.StringType()),
#     T.StructField("Customer_Email", T.StringType()),
#     T.StructField("Customer_Fname", T.StringType()),
#     T.StructField("Customer_Id", T.IntegerType()),
#     T.StructField("Customer_Lname", T.StringType()),
#     T.StructField("Customer_Password", T.StringType()),
#     T.StructField("Customer_Segment", T.StringType()),
#     T.StructField("Customer_State", T.StringType()),
#     T.StructField("Customer_Street", T.StringType()),
#     T.StructField("Customer_Zipcode", T.StringType()),
#     T.StructField("Department_Id", T.IntegerType()),
#     T.StructField("Department_Name", T.StringType()),
#     T.StructField("Latitude", T.FloatType()),
#     T.StructField("Longitude", T.FloatType()),
#     T.StructField("Market", T.StringType()),
#     T.StructField("Order_City", T.StringType()),
#     T.StructField("Order_Country", T.StringType()),
#     T.StructField("Order_Customer_Id", T.IntegerType()),
#     T.StructField("Order_date", T.TimestampType()),
#     T.StructField("Order_Id", T.IntegerType()),
#     T.StructField("Order_Item_Cardprod_Id", T.IntegerType()),
#     T.StructField("Order_Item_Discount", T.FloatType()),
#     T.StructField("Order_Item_Discount_Rate", T.FloatType()),
#     T.StructField("Order_Item_Id", T.IntegerType()),
#     T.StructField("Order_Item_Product_Price", T.FloatType()),
#     T.StructField("Order_Item_Profit_Ratio", T.FloatType()),
#     T.StructField("Order_Item_Quantity", T.IntegerType()),
#     T.StructField("Sales", T.FloatType()),
#     T.StructField("Order_Item_Total", T.FloatType()),
#     T.StructField("Order_Profit_Per_Order", T.FloatType()),
#     T.StructField("Order_Region", T.StringType()),
#     T.StructField("Order_State", T.StringType()),
#     T.StructField("Order_Status", T.StringType()),
#     T.StructField("Product_Card_Id", T.IntegerType()),
#     T.StructField("Product_Category_Id", T.IntegerType()),
#     T.StructField("Product_Description", T.StringType()),
#     T.StructField("Product_Image", T.StringType()),
#     T.StructField("Product_Name", T.StringType()),
#     T.StructField("Product_Price", T.FloatType()),
#     T.StructField("Product_Status", T.IntegerType()),
#     T.StructField("Shipping_date", T.TimestampType()),
#     T.StructField("Shipping_Mode", T.StringType())
# ])
