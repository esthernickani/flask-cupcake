
const submitBtn = document.querySelector('.submit-btn');
const allCakes = document.querySelectorAll('li');
submitBtn.addEventListener('click', addCupcake)

async function addCupcake(e) {
    /*Get form data */
    e.preventDefault()

    let flavor = document.getElementById('flavor').value;
    let size = document.getElementById('size').value;
    let image = document.getElementById('image').value;
    let rating = document.getElementById('rating').value;

    /*Post response to cupcakes api */
    const response = await axios.post(`/api/cupcakes`, {
        "flavor" : flavor,
        "size": size,
        "rating": rating,
        "image": image? image : none
    });

    /*empty form data*/
    document.getElementById('cupcake-add-form').reset();
}