from flask import Flask, jsonify, render_template
import snowflake.connector

snowflake_config = {
    'user': 'NITHIN',
    'password': 'Nithin@2024',
    'account': 'azqcwil-tf37140',
    'database': 'PRODUCTSDATA',
    'schema': 'PRODUCTSDATA.PUBLIC'
}

app = Flask(__name__)

def get_connection():
    try:
        return snowflake.connector.connect(**snowflake_config)
    except Exception as e:
        print("An error occurred while connecting with Snowflake:", e)
        return None

def get_companies_data():
    company_data = []
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM company_info")
            company_data = cursor.fetchall()
        except Exception as e:
            print("An error occurred while fetching the data:", e)
        finally:
            cursor.close()
            connection.close()
    return company_data

def get_company_by_name(company_name):
    company = None
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM company_info WHERE COMPANY_NAME = %s", (company_name,))
            company = cursor.fetchone()
        except Exception as e:
            print("An error occurred while searching for company name:", e)
        finally:
            cursor.close()
            connection.close()
    return company

def remove_company(company_name):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM company_info WHERE COMPANY_NAME = %s"
            cursor.execute(query, (company_name,))
            connection.commit()  # Commit here budy
            return True
        except Exception as e:
            print("An error occurred while deleting the company:", e)
            return False
        finally:
            cursor.close()
            connection.close()
    return False

@app.route('/')
def all_companies():
    company_data = get_companies_data()
    return render_template('index.html', company_data = company_data)

@app.route('/company/<string:company_name>')
def get_company(company_name):
    company_data = get_company_by_name(company_name)
    if company_data:
        return jsonify(company_data)
    else:
        return jsonify({"message": "Company not found"}), 404

@app.route('/company/delete/<string:company_name>')
def delete_company(company_name):
    if remove_company(company_name):
        return "Company deleted successfully", 200
    else:
        return "Company not found or deletion failed", 404

if __name__ == '__main__':
    app.run(debug=True)
