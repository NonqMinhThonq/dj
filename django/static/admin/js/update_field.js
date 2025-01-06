document.addEventListener('DOMContentLoaded', function() {
    const enterpriseSelect = document.querySelector('#id_enterprise');  // Lấy phần tử enterprise trong form
    const fieldSelect = document.querySelector('#id_field');  // Lấy phần tử field trong form

    if (enterpriseSelect && fieldSelect) {
        enterpriseSelect.addEventListener('change', function() {
            const enterpriseId = enterpriseSelect.value;
            if (enterpriseId) {
                fetch(`/admin/manage_matching/career/get_fields/` + enterpriseId)  // Tạo URL để lấy các field từ server
                    .then(response => response.json())
                    .then(data => {
                        fieldSelect.innerHTML = '';  // Làm rỗng các lựa chọn cũ trong field
                        data.fields.forEach(field => {
                            const option = document.createElement('option');
                            option.value = field;
                            option.text = field;
                            fieldSelect.appendChild(option);  // Thêm lựa chọn mới vào field
                        });
                    })
                    .catch(error => console.error('Error fetching fields:', error));
            } else {
                fieldSelect.innerHTML = '';  // Nếu không có enterprise, làm rỗng field
            }
        });
    }
});
