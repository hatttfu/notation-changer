const btn = document.getElementById('arrows')

btn.addEventListener('click', changeNotation)

function changeNotation() {

    // console.log('click')
    let numbers = Array.from(document.querySelectorAll('.number'))
    
    // numbers.forEach(element => {
    //     console.log(element.innerHTML)
    // });

    numbers[0].innerHTML == '2' ? numbers[0].innerHTML = '10' : numbers[0].innerHTML ='2'   
    numbers[1].innerHTML == '10' ? numbers[1].innerHTML ='2' : numbers[1].innerHTML ='10'   

    const query = new URLSearchParams(window. location.search); 
    query.append("enabled", "true");

}

