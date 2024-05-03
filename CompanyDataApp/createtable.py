import snowflake.connector

snowflake_config = {
    'user': 'NITHIN',
    'password': 'Nithin@2024',
    'account': 'azqcwil-tf37140',
    'database': 'PRODUCTSDATA',
    'schema': 'PUBLIC'
}

try:
    connection = snowflake.connector.connect(**snowflake_config)
    cursor = connection.cursor()

    # Create the table
    cursor.execute("""
    CREATE TABLE company_info( 
                           company_name VARCHAR,
        symbol VARCHAR,
        current_price VARCHAR,
        "52W high/low" VARCHAR,
        market_cap VARCHAR,
        industry VARCHAR)
    """)

    # Insert the data
    cursor.execute("""
    INSERT INTO company_info (company_name, symbol, current_price, "52W high/low", market_cap, industry)
    VALUES 
    ('3i Infotech Ltd.', '3IINFOLTD', '₹40.79 +5.15%', '₹63.89/₹30.69', '₹660 Crs', 'IT Services & Consulting'),
    ('63 Moons Technologies Ltd.', '63MOONS', '₹430 +0.59%', '₹690.75/₹162', '₹1967.55 Crs', 'IT Services & Consulting'),
    ('AAA Technologies Ltd.', 'AAATECH', '₹134.9 +1.09%', '₹147/₹50.7', '₹170.6 Crs', 'IT Services & Consulting'),
    ('ABM International Ltd.', 'ABMINTLLTD', '₹63.85 +3.06%', '₹74/₹31.35', '₹58.33 Crs', 'Trading & Distribution'),
    ('ADF Foods Ltd.', 'ADFFOODS', '₹226.09 -1.9%', '₹261.94/₹148', '₹2537.85 Crs', 'Food Products'),
    ('AION-TECH Solutions Ltd.', 'GOLDTECH', '₹129.65 +2.29%', '₹173.69/₹56.6', '₹439.19 Crs', 'IT Services & Consulting'),
    ('AKG Exim Ltd.', 'AKG', '₹20.6 +0.23%', '₹32.6/₹17.6', '₹66.73 Crs', 'Trading & Distribution'),
    ('AVG Logistics Ltd.', 'AVG', '₹542.85 -0.69%', '₹668.39/₹180', '₹747.08 Crs', 'Logistics'),
    ('AXISCADES Technologies Ltd.', 'AXISCADES', '₹640.35 +2.56%', '₹850/₹295.1', '₹2617.57 Crs', 'Software Services'),
    ('Accelya Solutions India Ltd.', 'ACCELYA', '₹1775.15 +0.28%', '₹2127.4/₹1251.45', '₹2641.95 Crs', 'Software Services'),
    ('Accuracy Shipping Ltd.', 'ACCURACY', '₹9 +0%', '₹18.25/₹7.04', '₹150.56 Crs', 'Logistics'),
    ('Adani Enterprises Ltd.', 'ADANIENT', '₹3072.55 +0.23%', '₹3350/₹1775.79', '₹349410.34 Crs', 'Trading & Distribution'),
    ('Aditya Birla Fashion and Retail Ltd.', 'ABFRL', '₹265.69 +0.82%', '₹273.19/₹184.4', '₹26796.25 Crs', 'Retailing'),
    ('Advani Hotels & Resorts (India) Ltd.', 'ADVANIHOTR', '₹83.75 +2.25%', '₹91.65/₹38.42', '₹758 Crs', 'Hotels'),
    ('Aeroflex Industries Ltd.', 'AEROFLEX', '₹147.8 +1.15%', '₹196.34/₹108', '₹1888.08 Crs', 'Iron & Steel'),
    ('Airan Ltd.', 'AIRAN', '₹27.19 -1.09%', '₹37/₹14', '₹350.06 Crs', 'IT Services & Consulting'),
    ('Airo Lam Ltd.', 'AIROLAM', '₹170 +0.27%', '₹196.8/₹66.5', '₹255.03 Crs', 'Wood Products'),
    ('Allcargo Gati Ltd.', 'ACLGATI', '₹107.25 +1.37%', '₹177.65/₹95.34', '₹1380.67 Crs', 'Logistics'),
    ('Allcargo Logistics Ltd.', 'ALLCARGO', '₹74.4 +0.27%', '₹98/₹61.4', '₹7272.59 Crs', 'Logistics'),
    ('Allcargo Terminals Ltd.', 'ATL', '₹60.39 +1.26%', '₹82.5/₹31.3', '₹1474.17 Crs', 'Logistics'),
    ('Allied Digital Services Ltd.', 'ADSL', '₹139.59 +0.82%', '₹201.25/₹78.54', '₹763.07 Crs', 'IT Services & Consulting'),
    ('Allsec Technologies Ltd.', 'ALLSEC', '₹748.1 +1.36%', '₹895/₹429.85', '₹1124.59 Crs', 'IT Services & Consulting')
    )
    """)

    cursor.close()
    connection.close()
except Exception as e:
    print("Error:", e)



import snowflake.connector

# Snowflake connection parameters
snowflake_config = {
    'user': 'NITHIN',
    'password': 'Nithin@2024',
    'account': 'azqcwil-tf37140',
    'database': 'PRODUCTSDATA',
    'schema': 'PRODUCTSDATA.PUBLIC'
}


product_data = [
    (12, 'Ground Beef (1lb)', 25, 6, 'Premium ground beef', 'https://img.freepik.com/premium-photo/uncooked-spiced-minced-meat-artistically-isolated-stark-white-background_829699-6768.jpg?w=740'),
    (13, 'Salmon Fillet', 15, 10, 'Fresh wild-caught salmon', 'https://img.freepik.com/free-photo/slice-raw-salmon_144627-11093.jpg?t=st=1713890953~exp=1713894553~hmac=f095a7e145f90dfaa1bcca31eca0f6d3afba4e7c52c25473b81aa2e0f45826b0&w=826'),
    (14, 'Pasta (Spaghetti)', 50, 2, 'Italian spaghetti pasta', 'https://img.freepik.com/premium-photo/organic-yellow-spaghetti-pasta-white-background_762785-130629.jpg?w=826'),
    (15, 'Rice (White)', 40, 3, 'Long-grain white rice', 'https://img.freepik.com/free-vector/rice-realistic-composition-with-mound-raw-white-paddy-near-cooked-porridge-bowl-decorated-by-green-sprout-vector-illustration_1284-77442.jpg?t=st=1713891112~exp=1713894712~hmac=9cacca40c0db4e2d37f5a90ea89928c709674155ce54088adc66686b1d55c572&w=1060'),
    (16, 'Black Beans', 30, 2.5, 'Dried black beans', 'https://img.freepik.com/free-photo/black-beans_1339-220.jpg?t=st=1713891151~exp=1713894751~hmac=d5d7b9ea1bbd9810f9d9d2bed59ec41218747e0ba28c77f99f1883915a4dcb56&w=826'),
    (17, 'Canned Tomatoes', 40, 1.5, 'Whole canned tomatoes', 'https://img.freepik.com/premium-photo/jar-with-pickled-tomatoes-white_185193-29728.jpg?w=826'),
    (18, 'Coffee (Ground)', 60, 4, 'Medium roast ground coffee', 'https://img.freepik.com/free-photo/top-view-portafilter-with-roasted-beans_23-2148336745.jpg?t=st=1713891254~exp=1713894854~hmac=9d7a8f947e87f2a83f7db03c30c5619658123f95123a150dc07e032effa6dacd&w=826'),
    (19, 'Tea (Green)', 30, 3, 'Loose-leaf green tea', 'https://img.freepik.com/premium-photo/green-tea-is-key-healthy-life-white-background_1061150-1984.jpg?w=740'),
    (20, 'Sugar (White)', 40, 2, 'Granulated white sugar', 'https://img.freepik.com/free-photo/marshmallows_2829-8021.jpg?t=st=1713891329~exp=1713894929~hmac=47a155f2ba1d64ee858709100c2e47ad265dd60420d541af9c9b1e68eb4437e7&w=740'),
    (21, 'Flour (All-Purpose)', 50, 2.5, 'Premium all-purpose flour', 'https://img.freepik.com/free-photo/ingredients-cook-recipe_144627-24735.jpg?t=st=1713891367~exp=1713894967~hmac=4b74f542084ed6b57f2c8cf998522199c33413618ff79906a51acad2014bebbd&w=740'),
    (22, 'Chocolate Chips', 25, 3.5, 'Semi-sweet chocolate chips', 'https://img.freepik.com/free-photo/cereals-chocolate-white-bowl_74190-4846.jpg?t=st=1713891398~exp=1713894998~hmac=11edf289c18a282ff5e72aed022307fb83a53408250a42fc3e453d3c1151ee15&w=826'),
    (23, 'PlayStation 5', 10, 500, 'Next-gen gaming console from Sony', 'https://img.freepik.com/premium-photo/top-view-generation-video-console-controller-isolated-white-dual-sense_462054-823.jpg?w=826'),
    (24, 'Nintendo Switch', 8, 300, 'Versatile gaming device from Nintendo', 'https://img.freepik.com/premium-photo/there-is-white-video-game-console-with-controller-it-generative-ai_1034578-43761.jpg?w=740'),
    (25, 'KitchenAid Mixer', 12, 350, 'Powerful and stylish mixer', 'https://img.freepik.com/free-vector/kitchen-appliances-electric-blender-whisk-household-equipment-cooking-food-mixer_107791-6644.jpg?t=st=1713891626~exp=1713895226~hmac=f7279229078384f2ea6f998dc2d909994848c580dfd45a995f83c965d4797fae&w=740'),
    (26, 'Instant Pot', 18, 150, 'Multi-functional electric pressure cooker', 'https://img.freepik.com/premium-photo/close-up-kettle-white-background_1048944-4245415.jpg?w=826'),
    (27, 'Cuisinart Knife Set', 25, 100, 'Premium stainless steel knife set', 'https://img.freepik.com/free-vector/butchers-knives-set-magnetic-holder-realistic-illustration_1284-59569.jpg?t=st=1713891686~exp=1713895286~hmac=66bdd8b23a538e90cf1b8452e9557acca6dfda5f49443e0d52a3422fbaa26360&w=740'),
    (28, 'Philips Air Fryer', 20, 200, 'Healthier frying with less oil', 'https://img.freepik.com/premium-photo/modern-toaster-isolated-white-background_506134-25769.jpg?w=826'),
    (29, 'Samsung Refrigerator', 5, 1500, 'Energy-efficient refrigerator', 'https://img.freepik.com/premium-photo/white-refrigerator-isolated-3d-rendering_461160-4337.jpg?w=740'),
    (30, 'LG Washing Machine', 7, 1000, 'Advanced washing machine from LG', 'https://img.freepik.com/free-photo/front-view-young-male-with-washer-dirty-clothes-white-wall_140725-107909.jpg?t=st=1713891816~exp=1713895416~hmac=5c4db24ba045d3d5394e26935205ca946d4f117056ed205acba123c6602e3827&w=360'),
    (31, 'Dyson Vacuum Cleaner', 10, 700, 'High-performance cordless vacuum', 'https://img.freepik.com/premium-photo/vacuum-cleaner-black-white-art-style-white-back_873925-898992.jpg?w=740'),
    (32, 'Sony 65" 4K Smart TV', 3, 2000, 'Immersive viewing experience', 'https://img.freepik.com/free-psd/modern-tv-screen-isolated_23-2151430360.jpg?t=st=1713891912~exp=1713895512~hmac=320ad420d331d956ff645815647f78038ef3ad9b1f0543e3b3d6ee864f991453&w=826'),
    (33, 'Bose Noise Cancelling', 15, 300, 'Premium noise-canceling headphones', 'https://img.freepik.com/free-psd/hearing-aids-still-life_23-2150634704.jpg?t=st=1713891945~exp=1713895545~hmac=66ce5be06b49ca332674c43c2f9d3809563de7b41313cb3d7b32bc4907fd12a4&w=826'),
    (34, 'JBL Portable Speaker', 20, 150, 'Portable and powerful Bluetooth speaker', 'https://img.freepik.com/premium-photo/close-up-cup-against-white-background_1048944-29056157.jpg?w=826'),
    (35, 'Canon EOS R5', 8, 3500, 'Professional-grade mirrorless camera', 'https://img.freepik.com/premium-photo/dslr-camera-white-background_223582-288.jpg?w=826'),
    (36, 'GoPro Hero 10', 12, 500, 'Action camera for capturing adventures', 'https://img.freepik.com/free-photo/front-view-hand-holding-virtual-reality-headset_23-2148775908.jpg?t=st=1713892107~exp=1713895707~hmac=4e83ae06b1b92f1740f585758345e676128e8751f5407fcd3fd90e265a262d1c&w=360'),
    (37, 'Fitbit Charge 5', 25, 200, 'Advanced fitness tracker', 'https://img.freepik.com/premium-photo/high-angle-view-smart-phone-against-white-background_1048944-13016870.jpg?w=826'),
    (38, 'Amazon Echo', 30, 100, 'Smart speaker with Alexa integration', 'https://img.freepik.com/premium-photo/modern-music-speaker-white-background_746318-6076.jpg?w=900'),
    (39, 'Google Nest Thermostat', 10, 250, 'Smart thermostat for home automation', 'https://img.freepik.com/free-photo/white-wireless-earbuds-with-case_53876-98557.jpg?t=st=1713892279~exp=1713895879~hmac=fc310bdeb5b06be9ade4a04c62902da2a004619735c4229e614a8b1c5d913c79&w=826'),
    (40, 'Acer Aspire 5', 15, 600, 'Budget-friendly laptop for everyday use', 'https://img.freepik.com/free-photo/laptop-with-white-screen-isolated-white-wall_231208-8590.jpg?t=st=1713892307~exp=1713895907~hmac=3a9f9235133e03fc99c2e1baa538fdd8b0ccca9c02e988c16bb1a676192773d4&w=826'),
    (41, 'Lenovo ThinkPad X1', 8, 1500, 'Premium business laptop from Lenovo', 'https://img.freepik.com/free-photo/top-view-laptop-with-white-background_23-2148236795.jpg?t=st=1713892351~exp=1713895951~hmac=74b41a3fd4c0f21108007c1524c6d2937a466405f3fc723ca025aaab1e7454a5&w=826'),
    (42, 'Asus ROG Strix G15', 5, 1200, 'Gaming laptop with high-performance specs', 'https://img.freepik.com/free-photo/mobile-screen-edge-laptop-with-mouse-white-background_23-2147854266.jpg?t=st=1713892397~exp=1713895997~hmac=0393957a8e17f10bbd19233c7eb89191aca445a4eb501ce20ac2fb97a531ffa9&w=826'),
    (43, 'HP Pavilion Desktop', 10, 800, 'Powerful desktop PC for productivity', 'https://img.freepik.com/free-photo/workplace-with-laptop-stand-near-eyeglasses_23-2148040478.jpg?t=st=1713892433~exp=1713896033~hmac=61d294c8641e77788c4795dd50f8b01fed0c2978bcc22cca8cb39e85702b3ecc&w=826'),
    (44, 'Samsung Galaxy Tab S7', 7, 700, 'Premium Android tablet from Samsung', 'https://img.freepik.com/premium-photo/digital-tablet-with-pencil-freelancer-artist-isolated-white-background-mockup-template-image-with-copy-space-photo_526934-620.jpg?w=826'),
    (45, 'iPad Air', 8, 600, 'Sleek and powerful tablet from Apple', 'https://img.freepik.com/free-vector/digital-device-mockup_53876-89924.jpg?t=st=1713892500~exp=1713896100~hmac=1361eb07232b542b8824be02d21f0e9272a58437aec4e12edf56a818649fc57a&w=740'),
    (46, 'Microsoft Surface Pro', 6, 900, 'Versatile 2-in-1 laptop and tablet', 'https://img.freepik.com/free-photo/top-view-tablet-wireless-keyboard_23-2148223212.jpg?t=st=1713892541~exp=1713896141~hmac=c8b9732aff73a16c3f88d147604d0732a7e93182ead0251f311b00b41d7ea17d&w=826'),
    (47, 'Asus Chromebook', 12, 400, 'Affordable and lightweight Chromebook', 'https://img.freepik.com/premium-photo/close-up-laptop-against-white-background_1048944-4656111.jpg?w=826')
]

try:
    # Connection with the snowflake budy
    conn = snowflake.connector.connect(**snowflake_config)
    cursor = conn.cursor()

    # updating produxts data_images
    for product in product_data:
        product_id, name, quantity, price, description, new_image_url = product
        cursor.execute("UPDATE PRODUCTS SET IMAGE_URL = %s WHERE PRODUCT_ID = %s", (new_image_url, product_id))
        conn.commit()

    # Close it now other wise..!
    cursor.close()
    conn.close()

    print("Product image URLs updated successfully!")

except snowflake.connector.errors.ProgrammingError as e:
    print("Snowflake programming error:", e)
except snowflake.connector.errors.DatabaseError as e:
    print("Snowflake database error:", e)
except snowflake.connector.errors.ForbiddenError as e:
    print("Snowflake forbidden error:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
