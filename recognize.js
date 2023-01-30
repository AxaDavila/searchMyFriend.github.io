//utilizar JavaScript para dibujar rectángulos alrededor de las caras detectadas en la imagen:
const image = document.getElementById("image");

// Aquí debes agregar código para detectar las caras en la imagen

// Dibujar un rectángulo alrededor de cada cara detectada
faces.forEach((face) => {
  const faceBox = document.createElement("div");
  faceBox.classList.add("face-box");
  faceBox.style.left = `${face.x}px`;
  faceBox.style.top = `${face.y}px`;
  faceBox.style.width = `${face.width}px`;
  faceBox.style.height = `${face.height}px`;
  image.parentElement.appendChild(faceBox);
});
