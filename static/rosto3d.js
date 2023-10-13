// rosto3d.js
const cena = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();

renderer.setSize(window.innerWidth, window.innerHeight);
document.getElementById('cena').appendChild(renderer.domElement);

const geometry = new THREE.BoxGeometry(); // Substitua isso pela geometria do rosto
const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 }); // Substitua isso pelo material do rosto
const cubo = new THREE.Mesh(geometry, material);

cena.add(cubo);
camera.position.z = 5;

const animate = function () {
    requestAnimationFrame(animate);

    // Adicione sua lógica de animação aqui

    renderer.render(cena, camera);
};

animate();
