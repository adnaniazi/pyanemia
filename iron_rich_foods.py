def foods():
    category_list = ['Baked products',
                     'Dairy products',
                     'Fats and oils',
                     'Fruits',
                     'Herbs and spices',
                     'Pulses and grains',
                     'Soups, sauces, and gravies',
                     'Sweets',
                     'Vegetables']
    list_of_foods_in_each_category = [['Chocolate-chip cookies', 'Cheese crackers', 'Wafers', 'Rust toast', 'Pastry', 'Sandwich'],
                                      ['Raw egg', 'Cheese', 'Milk powder', 'Milk shake', 'Cooked egg', 'Whole dried egg'],
                                      ['Regular butter', 'Salted butter', 'Butter without salt', 'Regular salads', 'Fat-free salad'],
                                      ['Cherries', 'Apples', 'Litchis', 'Ground cherries', 'Dates', 'Olives', 'Bananas', 'Apricots', 'Mulberries', 'Pears', 'Peaches', 'Plums'],
                                      ['Ginger', 'Garlic', 'Coriander seeds', 'Mustard', 'Dill seeds', 'Chili powder', 'Cardamon', 'Cumin seeds', 'Cloves'],
                                      ['Beans', 'Lima beans','Lentils', 'Mung beans', 'Corn', 'Beets', 'Jute', 'Rices', 'Wheat', 'Rye'],
                                      ['Onion gravy', 'Chicken gravy', 'Mushroom gravy', 'Chicken soup', 'Vegetable soup', 'Onion soup', 'Green pea soup'],
                                      ['Candies', 'Pudding','Baking chocolate', 'Coco powder', 'Gelatin powder', 'Custard'],
                                      ['Carrots', 'Green peas', 'Onions', 'Potatoes', 'Mushrooms', 'Spinach', 'Soy beans', 'Radish', 'Pumpkin', 'Broccoli', 'Cabbage', 'Papaya', 'Turnip']]
    list_of_iron_in_food_in_each_category = [[3.4, 4.77, 2.38, 2.72, 2.6, 2.72],
                                             [3.85, 1.9, 1.2, 7.7, 1.2, 8.28],
                                             [2, 1.09, 1.07, 1.08, 1.05],
                                             [1.26, 2, 1.7, 1, 1.02, 3.32, 1.15, 1.52, 1.85, 2.1, 1.2, 1.04],
                                             [11.52, 5.65, 16.32, 9.21, 16.33, 14.25, 13.97, 66.36, 8.68],
                                             [3, 5, 3.21, 1.9, 1.83, 1.82, 4.76, 1.46, 3.21, 2.63],
                                             [1, 1.33, 1.2, 1.87, 3.71, 1.25, 1.48],
                                             [1.23, 1.82, 2.91, 13.86, 1.11, 1.9],
                                             [1.09, 1.52, 1.54, 1.07, 1.72, 1.29, 1.5, 3.5, 6.73, 3.2, 1.27, 1.04, 6.14, 1.94]]
    return category_list, list_of_foods_in_each_category, list_of_iron_in_food_in_each_category
