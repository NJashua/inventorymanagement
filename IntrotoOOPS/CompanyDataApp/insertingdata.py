import snowflake.connector

snowflake_config = {
    'user': "NITHIN",
    'account': "azqcwil-tf37140",
    'password': "Nithin@2024",
    'database': "PRODUCTSDATA",
    'schema': "PUBLIC"
}

try:
    connection = snowflake.connector.connect(**snowflake_config)
    cursor = connection.cursor()
    cursor.execute(""" 
       INSERT INTO company_info (company_name, symbol, current_price, "52W high/low", market_cap, industry)
       VALUES
       ('Narmada Agrobase Ltd.', 'NARMADA', 0.23, '₹34.95/₹17.8', 32.52, 'Food Products'),
       ('National Steel and Agro Industries Ltd.', 'NATNLSTEEL', -2.47, '₹5.09/₹2.79', 17.8, 'Iron & Steel'),
       ('Navkar Corporation Ltd.', 'NAVKARCORP', 0.46, '₹125.54/₹53.5', 1625.61, 'Logistics'),
       ('Nazara Technologies Ltd.', 'NAZARA', 0.2, '₹989.39/₹540.7', 4944.59, 'IT Services & Consulting'),
       ('Nestle India Ltd.', 'NESTLEIND', 1.16, '₹2769.3/₹2030.79', 241135.71, 'Food Products'),
       ('Netweb Technologies India Ltd.', 'NETWEB', 0.66, '₹1892.59/₹500', 9345.46, 'IT Services & Consulting'),
       ('Newgen Software Technologies Ltd.', 'NEWGEN', -0.73, '₹489.46/₹290.1', 2629.85, 'IT Services & Consulting'),
       ('Next Mediaworks Ltd.', 'NEXTMEDIA', -1.24, '₹12.72/₹5.86', 16.15, 'Media & Entertainment'),
       ('NextGen Clothing Ltd.', 'NEXTGEN', 0.1, '₹20.07/₹12.25', 26.07, 'Textiles'),
       ('NFL Ltd.', 'NFL', 0.0, '₹35.15/₹18.1', 2845.09, 'Fertilizers'),
       ('NHPC Ltd.', 'NHPC', 0.79, '₹31.8/₹17.15', 81345.47, 'Power Generation/Distribution'),
       ('Nila Spaces Ltd.', 'NILASPACES', 0.0, '₹13.9/₹7.05', 26.78, 'Real Estate'),
       ('Nitin Castings Ltd.', 'NITINCAST', 0.15, '₹66.3/₹39.05', 203.12, 'Iron & Steel'),
       ('Nitin Spinners Ltd.', 'NITINSPIN', -2.05, '₹71.95/₹37.8', 372.55, 'Textiles'),
       ('NLC India Ltd.', 'NLCINDIA', -0.16, '₹63.1/₹29.75', 24697.26, 'Power Generation/Distribution'),
       ('NMDC Ltd.', 'NMDC', -2.07, '₹178.3/₹82.05', 36180.86, 'Mining & Minerals'),
       ('NOCIL Ltd.', 'NOCIL', -2.97, '₹238.8/₹139', 3183.16, 'Chemicals'),
       ('NOIDA TOLL BRIDGE COMPANY LTD.', 'NOIDATOLL', 0.07, '₹7.22/₹1.7', 19.91, 'Infrastructure General'),
       ('NTPC Ltd.', 'NTPC', -0.69, '₹143.65/₹82.7', 144524.82, 'Power Generation/Distribution'),
       ('NTPC Ltd.', 'NTPC', -0.69, '₹143.65/₹82.7', 144524.82, 'Power Generation/Distribution')
    """)

    cursor.close()
    connection.close()
    print("Data inserted successfully!")
except snowflake.connector.errors.Error as e:
    print("Error:", e)
