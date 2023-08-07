

function addToCart(product_id, quantity) {
    console.log("addToCart function called!");
    console.log("Product ID:", product_id);
    console.log("Quantity:", quantity);
    $.ajax({
        type: "POST",
        url: "/add_to_cart",
        data: {
            'product_item_id': product_id,
            'quantity': quantity,
        },
        dataType: "json",
        success: function (data) {
            if (data.success) {
                alert("Sản phẩm đã được thêm vào giỏ hàng!");
                location.reload();
            } else {
                alert("Có lỗi xảy ra khi thêm sản phẩm vào giỏ hàng!");
            }
        },
        error: function () {
            alert("Có lỗi xảy ra khi thêm sản phẩm vào giỏ hàng!");
        }
    });
}



function removeFromCart(productItemId) {
        console.log("removeFromCart function called!");
        console.log("Product Item ID:", productItemId);

        // Add your logic to remove the item from the cart here...

        // Example AJAX call to remove item
       $.ajax({
        type: "POST",
        url: "/remove_from_cart",
        data: {
            'product_item_id': productItemId,
        },
        dataType: "json",
        success: function (data) {
            if (data && data.success) {
                alert("Sản phẩm đã được xoá khỏi giỏ hàng!");
                location.reload();
            } else {
                alert("Có lỗi xảy ra khi xoá sản phẩm khỏi giỏ hàng!");
            }
        },
        error: function () {
            alert("Có lỗi xảy ra khi xoá sản phẩm khỏi giỏ hàng!");
        }
    });
    }


function updateQuantityCart(productItemId, quantity) {
console.log("updateQuantityCart called!");
  quantity = parseInt(quantity);

    console.log("Product Item ID:", productItemId);
    console.log("Quantity:", quantity);
    $.ajax({
        type: "POST",
        url: "/update_cart_item",
        data: {
            'product_item_id': productItemId,
            'quantity': quantity,
        },
        dataType: "json",
        success: function (data) {
            if (data.success) {
                // Refresh the cart page after successful update
                location.reload();
            } else {
                alert("Có lỗi xảy ra khi cập nhật số lượng!");
            }
        },
        error: function () {
            alert("Có lỗi xảy ra khi cập nhật số lượng!");
        }
    });
 console.log("Received Product Item ID:", productItemId);
    console.log("Received Quantity:", quantity);
}


document.getElementById("btnCreateOrder").addEventListener("click", function() {
    // Gọi hàm để đẩy thông tin giỏ hàng sang đơn hàng khi nút được bấm
    createOrderFromCart();
});

function createOrderFromCart() {
    // Lấy thông tin giỏ hàng từ trang giỏ hàng
    const cartData = getCartDataFromCartPage();

    // Gửi yêu cầu POST đến API để chuyển thông tin giỏ hàng sang đơn hàng
    fetch('/api/create_order', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(cartData),
    })
    .then((response) => response.json())
    .then((data) => {
        // Xử lý kết quả từ API nếu cần
        console.log(data);
        // Sau khi chuyển thành công, bạn có thể thực hiện hành động chuyển hướng sang trang đơn hàng hoặc thông báo thành công cho người dùng.
    })
    .catch((error) => console.error('Error:', error));
}

function getCartDataFromCartPage() {
    // Giả sử bạn có mã JavaScript để lấy thông tin giỏ hàng từ trang giỏ hàng.
    // Đoạn mã dưới đây chỉ để minh họa, bạn cần thay thế phần này bằng cách lấy thông tin giỏ hàng từ trang giỏ hàng của bạn.
    const cartData = {
        products: [
            {
                product_item_id: 1,
                quantity: 2,
            },
            {
                product_item_id: 2,
                quantity: 1,
            },
            // Thêm các sản phẩm khác vào danh sách nếu cần
        ],
    };

    return cartData;
}


   function login() {
        var login = $("input[name='login']").val();
        var password = $("input[name='password']").val();

        if (login && password) {
            // Gọi hàm authenticate thông qua Ajax request
            rpc.query({
                model: 'nhanvien',
                method: 'authenticate',
                args: [login, password],
            }).then(function(result) {
                if (result) {
                    // Đăng nhập thành công, chuyển hướng đến trang chủ
                    window.location.href = '/my_module/home';
                } else {
                    // Thông báo lỗi đăng nhập không hợp lệ
                    alert("Thông tin đăng nhập không hợp lệ. Vui lòng kiểm tra lại!");
                }
            });
        } else {
            // Thông báo lỗi thông tin đăng nhập trống
            alert("Vui lòng nhập đầy đủ thông tin đăng nhập!");
        }
    }