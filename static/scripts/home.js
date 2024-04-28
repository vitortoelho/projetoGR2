var campoA = document.getElementById('campoA');
var campoB = document.getElementById('campoB');
var btnConverter = document.querySelector('.Btn__home');

btnConverter.addEventListener('click', function() {
    var textoOriginal = campoA.value.toLowerCase();
    var textoModificado = textoOriginal.replace(/\b(carro|moto|caminhão|azul|branco|verde|preto|rosa)\b/g, function(match) {
        switch(match) {
            case 'carro':
                return 'car';
            case 'moto':
                return 'bike';
            case 'caminhão':
                return 'truck';
            case 'azul':
                return 'blue';
            case 'branco':
                return 'white';
            case 'verde':
                return 'green';
            case 'preto':
                return 'black';
            case 'rosa':
                return 'pink';
            default:
                return match;
        }
    });

    campoB.value = textoModificado;

    if (textoOriginal === '') {
        alert("Por favor, preencha o campo abaixo com alguma referência!");
    } else if (textoOriginal === textoModificado) {
        alert("Algum código que você escreveu não está em nosso banco de dados. Por favor, reveja o seu código.");
    }
});