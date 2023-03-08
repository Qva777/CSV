const initial_data = JSON.parse('{{ initial_data|escapejs }}');
        const formset_prefix = '{{ formset.prefix }}';
        for (let i = 0; i < initial_data.length; i++) {
            const data = initial_data[i];
            const prefix = formset_prefix + '-' + i;
            for (let key in data) {
                const input = document.querySelector(`[name=${prefix}-${key}]`);
                if (input) input.value = data[key];
            }
        }

const editForm = document.getElementById('edit-form');
editForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(editForm);
    try {
        const response = await fetch(editForm.action, {
            method: 'PATCH',
            body: formData,
        });
        const data = await response.json();
        if (data.success) {
            alert('Changes saved successfully!');
        } else {
            alert('Failed to save changes. Please try again.');
        }
    } catch (error) {
        console.error(error);
        alert('An error occurred while trying to save changes. Please try again later.');
    }
});

// delete_schema
document.getElementById('delete-schema-form').addEventListener('submit', function(event) {
      event.preventDefault();
      if (confirm('Are you sure you want to delete this schema?')) {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
          if (xhr.readyState === 4) {
            if (xhr.status === 200) {
              window.location.href = "{% url 'home' %}";
            } else {
              alert('An error occurred while deleting the schema. Please try again later.');
            }
          }
        };
        xhr.open('POST', "{% url 'delete_schema_ajax' schema.id %}");
        xhr.setRequestHeader('X-CSRFToken', "{{ csrf_token }}");
        xhr.send();
      }
    });