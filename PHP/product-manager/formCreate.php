<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>Create Product</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="main">
        <div class="form-container">
            <h2>Add Product</h2>
            <form action="create.php" method="get">
                <input type="text" name="productName" placeholder="Product Name" required />
                <input type="number" name="productID" placeholder="Product ID" required />
                <select name="qualityStatus" required>
                    <option value="" disabled selected>Select Quality</option>
                    <option value="damaged">Damaged</option>
                    <option value="moderate">Moderate</option>
                    <option value="good">Good</option>
                </select>
                <input type="url" name="pic" placeholder="Image URL" required />
                <input type="submit" value="Add Product" />
                <button type="button" onclick="window.location.href='view.php'">View Products</button>
            </form>
        </div>
    </div>
</body>
</html>
