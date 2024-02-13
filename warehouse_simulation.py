import random

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

random.seed(1)
no_of_objects = 10

# Initialize a 20x20 grid with None
warehouse = [[None for _ in range(20)] for _ in range(20)]

# Place objects in the grid
for i in range(no_of_objects + 1):
    while True:
        row, col = random.randint(0, 19), random.randint(0, 19)
        if warehouse[row][col] is None:
            warehouse[row][col] = chr(i + 64) if i > 0 else 'Robot'
            break

    if i > 0:
        while True:
            row, col = random.randint(0, 19), random.randint(0, 19)
            if warehouse[row][col] is None:
                warehouse[row][col] = f"{chr(i + 64)}-D"
                break


@app.route('/')
def warehouse_map():
    return render_template('warehouse.html', warehouse=warehouse)

@app.route('/move_object', methods=['POST'])
def move_object():
    data = request.get_json()

    print(warehouse)

    row, col = data['row'], data['col']

    # Implement logic to move object or robot based on row and col
    # Update warehouse dictionary accordingly

    # Example: Swap object A and B positions
    if warehouse[2][3] is not None and warehouse[4][2] is not None:
        warehouse[2][3], warehouse[4][2] = warehouse[4][2], warehouse[2][3]

    print(warehouse)

    return jsonify(warehouse=warehouse)

if __name__ == '__main__':
    app.run(debug=True)
