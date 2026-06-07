qty → quantity sold (demand)
      "how many units were sold this month"
      This is what your model predicts

unit_price  → YOUR product's price
              "you're selling at ₹299"

comp_1      → Competitor 1's price
comp_2      → Competitor 2's price  
comp_3      → Competitor 3's price
              "amazon selling same thing at ₹259"

lag_price   → YOUR price last month
              "last month you sold at ₹279"

freight_price → Shipping cost
                "customer pays ₹40 extra to ship"

product_id              → Which product
                          "bed1, health3 etc"

product_category_name   → Which category
                          9 types:
                          bed_bath_table
                          garden_tools
                          consoles_games
                          health_beauty
                          cool_stuff
                          perfumery
                          computers_accessories
                          watches_gifts
                          furniture_decor

product_score           → Customer rating (3.3 to 4.5)
                          Higher rating = more sales
                          regardless of price

product_name_lenght     → How long product name is
                          (longer = more descriptive)

product_description_lenght → How detailed description is
                             (more detail = more trust)

product_photos_qty      → Number of photos
                          (more photos = more sales)

product_weight_g        → Weight in grams
                          (affects shipping cost)

volume                  → Physical size of product

month_year    → "01-05-2017" when this data was recorded

month         → 1 to 12 (January to December)
year          → 2017, 2018 etc

weekday       → How many weekday days in that month
weekend       → How many weekend days in that month
holiday       → Was there a holiday? (0 or 1)

total_price   → Total revenue that month
                unit_price × qty = total_price

customers     → Number of unique customers
                (different from qty — one customer
                can buy multiple units)

ps1  → Competitor 1's product score/rating
ps2  → Competitor 2's product score/rating
ps3  → Competitor 3's product score/rating

fp1  → Competitor 1's freight/shipping price
fp2  → Competitor 2's freight/shipping price
fp3  → Competitor 3's freight/shipping price