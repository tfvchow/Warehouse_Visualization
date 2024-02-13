from flask import Flask, render_template

app = Flask(__name__)

# Sample warehouse data
warehouse = {
    (1, 1): 'Robot',  # Black dot for robot
    (2, 3): 'Object A (Transparent)',  # Transparent text
    (4, 2): 'Object B (Grey)',  # Grey text
}

@app.route('/')
def warehouse_map():
    return render_template('warehouse.html', warehouse=warehouse)

if __name__ == '__main__':
    app.run(debug=True)
