#See the two tab delimited files attached:
#products.tab = A list of product names tab delimited with categories
#sales.tab = A list of product names tab delimited with sales amount
#From this data we'd like you to answer two questions:
#What are the top 5 categories by sales
#What is the top product by sales in category 'Candy'
#This comes from when I worked at a company that made back office software for restaurants.
#You can imagine the second file is a Point of Sale record for the day.

#Product class represents each product with fields names, amount, category
class Product
    attr_accessor :name, :amount, :category
    @@hsh = {}

    #constructor
    def initialize name, amount
        @name = name
        @amount = amount.to_f
    end

    #Getter method that returns the completed hash
    def self.get_all_products
        return @@hsh
    end

    #Parses sales.tab and creates object with product name and sales amount fields
    def self.create_sales file_name
        if File.exists? file_name
            fd = File.open file_name, "r"
        else
            puts "Usage: ./challenge.rb\nFiles sales.tab and products.tab must be in the same directory"
            exit
        end
        fd.each_line do |line|
            product = line.split "\t"
            if product.size == 2 and not @@hsh[product[0]]
                @@hsh[product[0]] = Product.new product[0], product[1]
            end
        end
        fd.close
    end
    #Parses products.tab and applies category to each product object
    def self.read_product file_name
        if File.exists? file_name
            fd = File.open file_name, "r"
        else
            puts "Usage: ./challenge.rb\nFiles sales.tab and products.tab must be in the same directory"
            exit
        end
        fd.each_line do |line|
            product = line.split "\t"
            if product.size == 2
                @@hsh[product[0]].category = product[1].strip if @@hsh[product[0]]
            end
        end
        fd.close
    end

end

#Main where everything happens
Product.create_sales("sales.tab")
Product.read_product("products.tab")
all_products = Product.get_all_products

#Create empty hash. Categories should take on the product category and the product amount as the key, value pair.
categories = {}

#Goes through products hash table and sets and increments the value for each product
all_products.each_value do |product|
    if categories[product.category]
        categories[product.category] += product.amount
    else
        categories[product.category] = product.amount
    end
end

#initializes a max tuple with a string field representing the candy and number
#field representing the total
max = ["", 0]

#goes through the product hash and finds the max number amount for the candy field
all_products.each_value do |product|
    begin
        if product.category.casecmp("Candy") == 0
            if product.amount > max[1]
                max = [product.name, product.amount]
            end
        end
    rescue
        nil
    end
end

#sort categories by sale
categories = categories.sort_by{|category, sales| sales}

#take top 5 in Descending order from the categories
top_five = categories.reverse[0, 5]

top_five.each {|category, sales| puts "\n#{category}: #{sales}"}
puts "\nTop product by sales in category 'Candy': \n#{max[0]}\nwith value $ #{max[1]}"
