async function loadFile(file) {
	text = await file.text();
	text=text.replaceAll('/', ' ');
	text=text.replaceAll('\n', ' ');
	let arrayCopy = text.split(' ');
	const vertices = [[]]; let licz_vertices = 0;
	const normals = [[]]; let licz_normals = 0;
	const coords = [[]]; let licz_coords = 0;
	const triangles = []; let licz_triangles = 0;
	for (let i=0;i<arrayCopy.length-1;i++)
	{
		if (arrayCopy[i]=='v') {
	vertices.push([]);
	vertices[licz_vertices].push(parseFloat(arrayCopy[i+1]));
	vertices[licz_vertices].push(parseFloat(arrayCopy[i+2]));
	vertices[licz_vertices].push(parseFloat(arrayCopy[i+3]));
	i+=3;
	licz_vertices++;
	}
		if (arrayCopy[i]=='vn') {
	normals.push([]);
	normals[licz_normals].push(parseFloat(arrayCopy[i+1]));	
	normals[licz_normals].push(parseFloat(arrayCopy[i+2]));
	normals[licz_normals].push(parseFloat(arrayCopy[i+3]));
	i+=3;
	licz_normals++;
	}
		if (arrayCopy[i]=='vt') {
	coords.push([]);
	coords[licz_coords].push(parseFloat(arrayCopy[i+1]));
	coords[licz_coords].push(parseFloat(arrayCopy[i+2]));
	i+=2;
	licz_coords++;
	}
		if (arrayCopy[i]=='f') {
	triangles.push([]);
	for (let j=1;j<=9;j++)
	triangles[licz_triangles].push(parseFloat(arrayCopy[i+j]));
	i+=9;
	licz_triangles++;
	}
}
	let vert_array=[];
	for (let i = 0; i < triangles.length; i++)
	{
	vert_array.push(vertices[triangles[i][0] - 1][0]);
	vert_array.push(vertices[triangles[i][0] - 1][1]);
	vert_array.push(vertices[triangles[i][0] - 1][2]);
	vert_array.push(normals[triangles[i][2] - 1][0]);
	vert_array.push(normals[triangles[i][2] - 1][1]);
	vert_array.push(normals[triangles[i][2] - 1][2]);
	vert_array.push(coords[triangles[i][1] - 1][0]);
	vert_array.push(coords[triangles[i][1] - 1][1]);
	vert_array.push(vertices[triangles[i][3] - 1][0]);
	vert_array.push(vertices[triangles[i][3] - 1][1]);
	vert_array.push(vertices[triangles[i][3] - 1][2]);
	vert_array.push(normals[triangles[i][5] - 1][0]);
	vert_array.push(normals[triangles[i][5] - 1][1]);
	vert_array.push(normals[triangles[i][5] - 1][2]);
	vert_array.push(coords[triangles[i][4] - 1][0]);
	vert_array.push(coords[triangles[i][4] - 1][1]);
	vert_array.push(vertices[triangles[i][6] - 1][0]);
	vert_array.push(vertices[triangles[i][6] - 1][1]);
	vert_array.push(vertices[triangles[i][6] - 1][2]);
	vert_array.push(normals[triangles[i][8] - 1][0]);
	vert_array.push(normals[triangles[i][8] - 1][1]);
	vert_array.push(normals[triangles[i][8] - 1][2]);
	vert_array.push(coords[triangles[i][7] - 1][0]);
	vert_array.push(coords[triangles[i][7] - 1][1]);
	}
	points=triangles.length*3;
	gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vert_array), gl.STATIC_DRAW);
}



let points = 36;
let gl;

function start() {

const vertexShader = `#version 300 es
precision mediump float;
uniform mat4 model;
uniform mat4 view;
uniform mat4 proj;
in vec3 position;
in vec3 color;
out vec3 Color;
in vec2 aTexCoord;
out vec2 TexCoord;
void main(void)
{
	TexCoord = aTexCoord;
	Color = color;
	gl_Position = proj*view*model*vec4(position, 1.0);
}	
`;

const fragmentShader = `#version 300 es
precision mediump float;
out vec4 frag_color;
in vec3 Color;
in vec2 TexCoord;
uniform sampler2D texture1;
uniform sampler2D texture2;
void main(void)
{
	frag_color = mix(texture(texture1, TexCoord),texture(texture2, TexCoord),0.5);
	//frag_color = vec4(Color, 1.0);
}
`;

            const canvas = document.getElementById("my_canvas");

			//Inicialize the GL contex
            gl = canvas.getContext("webgl2");

			if (gl === null) {
				alert("Unable to initialize WebGL. Your browser or machine may not support it.");
			//return;
			}

			console.log("WebGL version: " + gl.getParameter(gl.VERSION));
            console.log("GLSL version: " + gl.getParameter(gl.SHADING_LANGUAGE_VERSION));
            console.log("Vendor: " + gl.getParameter(gl.VENDOR));


            const vs = gl.createShader(gl.VERTEX_SHADER);
            const fs = gl.createShader(gl.FRAGMENT_SHADER);
            const program = gl.createProgram();


//compilation vs
		gl.shaderSource(vs, vertexShader);
		/*var vertexShaderSource = document.querySelector("#vs").text;*/

		gl.compileShader(vs);

		if(!gl.getShaderParameter(vs, gl.COMPILE_STATUS))
                {
                    alert(gl.getShaderInfoLog(vs));
                }

//compilation fs
		gl.shaderSource(fs, fragmentShader);
        
				gl.compileShader(fs);

		if(!gl.getShaderParameter(fs, gl.COMPILE_STATUS))
                {
                    alert(gl.getShaderInfoLog(fs));
                }

            gl.attachShader(program, vs);
            gl.attachShader(program, fs);
            gl.linkProgram(program);
			

            if(!gl.getProgramParameter(program, gl.LINK_STATUS))
            {
                alert(gl.getProgramInfoLog(program));
            }

          
            const buffer = gl.createBuffer();
            gl.bindBuffer(gl.ARRAY_BUFFER, buffer);

						var n_draw=3;
						kostka();
						
						gl.useProgram(program);
			//macierz modelu
			const model = mat4.create();
			const kat_obrotu = 0;
			mat4.rotate(model, model, kat_obrotu, [0,0,1]);
			
			//macierz widoku
			const view = mat4.create(); 
			mat4.lookAt(view, [0,0,3], [0,0,-1], [0,1,0]);
			
			let uniView = gl.getUniformLocation(program, 'view');
			gl.uniformMatrix4fv( uniView, false, view);
			
			//macierz projekcji
			const proj = mat4.create();
			mat4.perspective(proj, 60 * Math.PI / 180, gl.canvas.clientWidth / gl.canvas.clientHeight, 0.1, 100.0 );
			
			let uniProj = gl.getUniformLocation(program, 'proj');       
			gl.uniformMatrix4fv( uniProj, false, proj);
			
			let uniModel = gl.getUniformLocation(program, 'model');       
			gl.uniformMatrix4fv( uniModel, false, model);

            const position = gl.getAttribLocation(program, "position");
            gl.enableVertexAttribArray(position);
            gl.vertexAttribPointer(position, 3, gl.FLOAT, false, 8*4, 0);

			const colorAttrib = gl.getAttribLocation(program, "color");
            gl.enableVertexAttribArray(colorAttrib);            
			gl.vertexAttribPointer(colorAttrib, 3, gl.FLOAT, false, 8*4, 3*4);
			
			const texCoord = gl.getAttribLocation(program, "aTexCoord");
			gl.enableVertexAttribArray(texCoord);
			gl.vertexAttribPointer(texCoord, 2, gl.FLOAT, false, 8*4, 6*4);

			var	primitive = 0;
			FPS = 30 //limit fps
			setTimeout(() => { requestAnimationFrame(draw);}, 1000 / FPS);
			
			
			let licznik=0;
			const fpsElem = document.querySelector("#fps");
			
			let startTime=0;
			let elapsedTime=0;

			let mode = 2;
			
			let separateLeft = -6.0;
			let separateRight = 6.0;
			let seperateBottom = -4.8;
			let seperateTop = 4.8;
			let eyeRed = -0.1;
			let eyeBlue = 0.1;
			
	    function draw()
            {
				elapsedTime = performance.now() - startTime;
                gl.clearColor(0, 0, 0, 1);
                gl.clear(gl.COLOR_BUFFER_BIT);
				gl.clear(gl.DEPTH_BUFFER_BIT);
                
				gl.useProgram(program);
                gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
				
				gl.activeTexture(gl.TEXTURE0);
				
				gl.bindTexture(gl.TEXTURE_2D, texture2);
				gl.drawArrays(gl.TRIANGLES, 0, points);
				
			/*	gl.bindTexture(gl.TEXTURE_2D, texture1);
				gl.drawArrays(gl.TRIANGLES, 0, 18);
               
				gl.bindTexture(gl.TEXTURE_2D, texture2);
				gl.drawArrays(gl.TRIANGLES, 18, 18)
			*/
			/*	gl.bindTexture(gl.TEXTURE_2D, texture1);
				gl.activeTexture(gl.TEXTURE1);
				gl.bindTexture(gl.TEXTURE_2D, texture2);
				gl.drawArrays(gl.TRIANGLES, 0, 36);
			*/		
			
			
			
			switch(mode)
			{
				case 0: //blue and red - stereo
				gl.viewport(0, 0, canvas.width, canvas.height);
				
				StereoProjection(separateLeft, separateRight, seperateBottom, seperateTop, 12.99, -100, 0, 13, eyeRed);
				gl.colorMask(true,false,false,false);
				
			//	gl.bindTexture(gl.TEXTURE_2D, texture1);
			//	gl.activeTexture(gl.TEXTURE1);
				gl.clear(gl.DEPTH_BUFFER_BIT);
				gl.bindTexture(gl.TEXTURE_2D, texture2);
				gl.drawArrays(gl.TRIANGLES, 0, points);
				
				gl.clear(gl.DEPTH_BUFFER_BIT);
				StereoProjection(separateLeft, separateRight, seperateBottom, seperateTop, 12.99, -100, 0, 13, eyeBlue);
				gl.colorMask(false,false,true,false);
				
			//	gl.bindTexture(gl.TEXTURE_2D, texture1);
			//	gl.activeTexture(gl.TEXTURE1);
				gl.clear(gl.DEPTH_BUFFER_BIT);
				gl.bindTexture(gl.TEXTURE_2D, texture2);
				gl.drawArrays(gl.TRIANGLES, 0, points);
				
				gl.colorMask(true,true,true,true);
				
				break;
				case 1: //side by side
				
				gl.viewport(canvas.width/2, 0, canvas.width/2, canvas.height);
				
				StereoProjection(separateLeft, separateRight, seperateBottom, seperateTop, 12.99, -100, 0, 13, -0.1);
				//StereoProjection(-6, 6, -4.8, 4.8, 12.99, -100, 0, 13, -0.1);
				
			//	gl.bindTexture(gl.TEXTURE_2D, texture1);
			//	gl.activeTexture(gl.TEXTURE1);
				gl.clear(gl.DEPTH_BUFFER_BIT);
				gl.bindTexture(gl.TEXTURE_2D, texture2);
				gl.drawArrays(gl.TRIANGLES, 0, points);
				
				gl.clear(gl.DEPTH_BUFFER_BIT);
				StereoProjection(separateLeft, separateRight, seperateBottom, seperateTop, 12.99, -100, 0, 13, 0.1);
				
				
				gl.viewport(0, 0, canvas.width/2, canvas.height);
				
			//	gl.bindTexture(gl.TEXTURE_2D, texture1);
			//	gl.activeTexture(gl.TEXTURE1);
				gl.clear(gl.DEPTH_BUFFER_BIT);
				gl.bindTexture(gl.TEXTURE_2D, texture2);
				gl.drawArrays(gl.TRIANGLES, 0, points);
				
				
				
				break;
				case 2: // mono
				gl.viewport(0, 0, canvas.width, canvas.height);
				//gl.bindTexture(gl.TEXTURE_2D, texture1);
				gl.activeTexture(gl.TEXTURE0);
				
				
				gl.bindTexture(gl.TEXTURE_2D, texture2);
				gl.drawArrays(gl.TRIANGLES, 0, 774);
				
				
				
				gl.bindTexture(gl.TEXTURE_2D, texture1);
				gl.drawArrays(gl.TRIANGLES, 774, 6);
				
				//console.log(points);//780 774
				
				break;
			}

			
			
			
				startTime = performance.now();

				ustaw_kamere();
				
				licznik++;
				let fFps = 1000 / elapsedTime; 
				if(licznik > fFps){ // ograniczenie częstotliwości odświeżania napisu do ok 1/s
				fpsElem.textContent = fFps.toFixed(1);
				licznik = 0;
				}
				//window.requestAnimationFrame(draw);
				setTimeout(() => { requestAnimationFrame(draw);}, 1000 / FPS);
            }
			
			
			
			function kostka() {
let punkty_ = 36;
var vertices = [
-0.5, -0.5, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0,
 0.5, -0.5, -0.5, 0.0, 0.0, 1.0, 1.0, 0.0,
 0.5, 0.5, -0.5, 0.0, 1.0, 1.0, 1.0, 1.0,
 0.5, 0.5, -0.5, 0.0, 1.0, 1.0, 1.0, 1.0,
-0.5, 0.5, -0.5, 0.0, 1.0, 0.0, 0.0, 1.0,
-0.5, -0.5, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0,
-0.5, -0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0,
 0.5, -0.5, 0.5, 1.0, 0.0, 1.0, 1.0, 0.0,
 0.5, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0,
 0.5, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0,
-0.5, 0.5, 0.5, 0.0, 1.0, 0.0, 0.0, 1.0,
-0.5, -0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0,
-0.5, 0.5, 0.5, 1.0, 0.0, 1.0, 0.0, 0.0,
-0.5, 0.5, -0.5, 1.0, 1.0, 1.0, 1.0, 0.0,
-0.5, -0.5, -0.5, 0.0, 1.0, 0.0, 1.0, 1.0,
-0.5, -0.5, -0.5, 0.0, 1.0, 0.0, 1.0, 1.0,
-0.5, -0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0,
-0.5, 0.5, 0.5, 1.0, 0.0, 1.0, 0.0, 0.0,
 0.5, 0.5, 0.5, 1.0, 0.0, 1.0, 0.0, 0.0,
 0.5, 0.5, -0.5, 1.0, 1.0, 1.0, 1.0, 0.0,
 0.5, -0.5, -0.5, 0.0, 1.0, 0.0, 1.0, 1.0,
 0.5, -0.5, -0.5, 0.0, 1.0, 0.0, 1.0, 1.0,
 0.5, -0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0,
 0.5, 0.5, 0.5, 1.0, 0.0, 1.0, 0.0, 0.0,
-0.5, -0.5, -0.5, 0.0, 1.0, 0.0, 0.0, 0.0,
 0.5, -0.5, -0.5, 1.0, 1.0, 1.0, 1.0, 0.0,
 0.5, -0.5, 0.5, 1.0, 0.0, 1.0, 1.0, 1.0,
 0.5, -0.5, 0.5, 1.0, 0.0, 1.0, 1.0, 1.0,
-0.5, -0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0,
-0.5, -0.5, -0.5, 0.0, 1.0, 0.0, 0.0, 0.0,
-0.5, 0.5, -0.5, 0.0, 1.0, 0.0, 0.0, 0.0,
 0.5, 0.5, -0.5, 1.0, 1.0, 1.0, 1.0, 0.0,
 0.5, 0.5, 0.5, 1.0, 0.0, 1.0, 1.0, 1.0,
 0.5, 0.5, 0.5, 1.0, 0.0, 1.0, 1.0, 1.0,
-0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0,
-0.5, 0.5, -0.5, 0.0, 1.0, 0.0, 0.0, 0.0
];

gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW);
n_draw=punkty_;
}

let cameraPos = glm.vec3(0,0,3);
let cameraFront = glm.vec3(0,0,-1);
let cameraUp = glm.vec3(0,1,0);
let obrot=0.0;
			
		/*	window.addEventListener('mousedown', e => {
  
			if (gl.isEnabled(gl.DEPTH_TEST)) gl.disable(gl.DEPTH_TEST);
			else gl.enable(gl.DEPTH_TEST);
			});
			*/
			gl.enable(gl.DEPTH_TEST);
			var pressedKey = {};
			window.onkeyup = function(e) { pressedKey[e.keyCode] = false;
			}
			window.onkeydown = function(e) { pressedKey[e.keyCode] = true; 
			}
			
			function ustaw_kamere() {
			let cameraSpeed = 0.002*elapsedTime;
			if (pressedKey["38"]) //Up
			{cameraPos.x+=cameraSpeed * cameraFront.x;
			cameraPos.y+=cameraSpeed * cameraFront.y;
			cameraPos.z+=cameraSpeed * cameraFront.z;}
			else if (pressedKey["37"]) //Left
			{
			let cameraPos_tmp = glm.normalize(glm.cross(cameraFront, cameraUp));
			cameraPos.x-=cameraPos_tmp.x * cameraSpeed;
			cameraPos.y-=cameraPos_tmp.y * cameraSpeed;
			cameraPos.z-=cameraPos_tmp.z * cameraSpeed; }
			else if (pressedKey["39"]) //Right
			{let cameraPos_tmp = glm.normalize(glm.cross(cameraFront, cameraUp));
			cameraPos.x+=cameraPos_tmp.x * cameraSpeed;
			cameraPos.y+=cameraPos_tmp.y * cameraSpeed;
			cameraPos.z+=cameraPos_tmp.z * cameraSpeed; }
			else if (pressedKey["40"]) //Down
			{cameraPos.x-=cameraSpeed * cameraFront.x;
			cameraPos.y-=cameraSpeed * cameraFront.y;
			cameraPos.z-=cameraSpeed * cameraFront.z;}
			
			let cameraFront_tmp = glm.vec3(1,1,1);
			
			cameraFront_tmp.x = cameraPos.x+cameraFront.x;
			cameraFront_tmp.y = cameraPos.y+cameraFront.y;
			cameraFront_tmp.z = cameraPos.z+cameraFront.z;
			
			mat4.lookAt(view, cameraPos, cameraFront_tmp, cameraUp);
			gl.uniformMatrix4fv( uniView, false, view);
			
			}
			//requestAnimationFrame(ustaw_kamere);
			
			canvas.requestPointerLock = canvas.requestPointerLock ||
			canvas.mozRequestPointerLock;
			
			document.exitPointerLock = document.exitPointerLock ||
			document.mozExitPointerLock;
			
			canvas.onclick = function() {
			canvas.requestPointerLock();
			};
			// Hook pointer lock state change events for different browsers
			document.addEventListener('pointerlockchange', lockChangeAlert, false);
			document.addEventListener('mozpointerlockchange', lockChangeAlert, false);

			function lockChangeAlert() {
				
			if (document.pointerLockElement === canvas ||
			document.mozPointerLockElement === canvas) {
			console.log('The pointer lock status is now locked');
			document.addEventListener("mousemove", ustaw_kamere_mysz, false);
			} else {
			console.log('The pointer lock status is now unlocked');
			document.removeEventListener("mousemove", ustaw_kamere_mysz, false);
			}
}
			let x = 50; //zmiana położenia w kierunku x
			let y = 50; //zmiana położenia w kierunku y
			
			let yaw =-90; //obrót względem osi X
			let pitch=0; //obrót względem osi Y
			
			
			function ustaw_kamere_mysz(e) {
				
			let xoffset = e.movementX;
			let yoffset = e.movementY;
			let sensitivity = 0.1;
			let cameraSpeed = 0.05*elapsedTime;
			
			xoffset *= sensitivity;
			yoffset *= sensitivity;

			yaw += xoffset * cameraSpeed;
			pitch -= yoffset*cameraSpeed;
			
			if (pitch > 89.0) pitch = 89.0;
			
			if (pitch < -89.0) pitch = -89.0;

			let front = glm.vec3(1,1,1);
			
			front.x = Math.cos(glm.radians(yaw))*Math.cos(glm.radians(pitch));
			front.y = Math.sin(glm.radians(pitch));
			front.z = Math.sin(glm.radians(yaw)) * Math.cos(glm.radians(pitch));
			cameraFront = glm.normalize(front);
			}
// textury
			const texture1 = gl.createTexture();
			gl.bindTexture(gl.TEXTURE_2D, texture1);
			const level = 0;
			const internalFormat = gl.RGBA;
			const width = 1;
			const height = 1;
			const border = 0;
			const srcFormat = gl.RGBA;
			const srcType = gl.UNSIGNED_BYTE;
			const pixel = new Uint8Array([0, 0, 255, 255]);
			gl.texImage2D(gl.TEXTURE_2D, level, internalFormat,
						width, height, border, srcFormat, srcType,
						pixel);
			const image = new Image();
			image.onload = function() {
			gl.bindTexture(gl.TEXTURE_2D, texture1);
			gl.texImage2D(gl.TEXTURE_2D, level, internalFormat,srcFormat, srcType, image);

			gl.generateMipmap(gl.TEXTURE_2D);
			gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.REPEAT);
			gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.REPEAT);
			gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
			gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
			};
			image.crossOrigin = "";
			image.src = "https://cdn.pixabay.com/photo/2013/09/22/19/14/brick-wall-185081_960_720.jpg";


			const texture2 = gl.createTexture();
			gl.bindTexture(gl.TEXTURE_2D, texture2);
			const level2 = 0;
			const internalFormat2 = gl.RGBA;
			const width2 = 1;
			const height2 = 1;
			const border2 = 0;
			const srcFormat2 = gl.RGBA;
			const srcType2 = gl.UNSIGNED_BYTE;
			const pixel2 = new Uint8Array([0, 0, 255, 255]);
			gl.texImage2D(gl.TEXTURE_2D, level2, internalFormat2,
						width2, height2, border2, srcFormat2, srcType2,
						pixel2);
			const image2 = new Image();
			image2.onload = function() {
			gl.bindTexture(gl.TEXTURE_2D, texture2);
			gl.texImage2D(gl.TEXTURE_2D, level2, internalFormat2,srcFormat2, srcType2, image2);

			gl.generateMipmap(gl.TEXTURE_2D);
			gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.REPEAT);
			gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.REPEAT);
			gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
			gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
			};
			image2.crossOrigin = "";
			image2.src = "https://images.pexels.com/photos/866351/pexels-photo-866351.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260";

			gl.uniform1i(gl.getUniformLocation(program, "texture1"), 0);
			gl.uniform1i(gl.getUniformLocation(program, "texture2"), 1);

			//requestAnimationFrame(ustaw_kamere);
			
			
			//3DDDDDDDDDDDDDDDDDDD
			function StereoProjection(_left, _right, _bottom, _top, _near, _far, _zero_plane, _dist, _eye)
			{
			
			let _dx = _right - _left;
			let _dy = _top - _bottom;
			
			let _xmid = (_right + _left) / 2.0;
			let _ymid = (_top + _bottom) / 2.0;
			
			let _clip_near = _dist + _zero_plane - _near;
			let _clip_far = _dist + _zero_plane - _far;
			
			let _n_over_d = (_clip_near / _dist);
			
			let _topw = _n_over_d * _dy / 2.0;
			let _bottomw = -_topw;
			let _rightw = _n_over_d * (_dx / 2.0 - _eye);
			let _leftw = _n_over_d * (-_dx / 2.0 - _eye);
			
			const proj = mat4.create();
			
			mat4.frustum(proj, _leftw, _rightw, _bottomw, _topw, _clip_near, _clip_far)
			mat4.translate(proj, proj, [-_xmid - _eye, -_ymid, 0]);
			
			let uniProj = gl.getUniformLocation(program, 'proj');
			gl.uniformMatrix4fv( uniProj, false, proj);
			}
			window.addEventListener('keydown', function(event) {
			//alert(event.keyCode);
			switch (event.keyCode) {
			case 77:
			mode++;
			if(mode>2) mode = 0;
			break;
			case 81:
			eyeRed+=0.1;
			eyeBlue-=0.1;
			break;
			case 87:
			eyeRed-=0.1;
			eyeBlue+=0.1;
			break;
		/*	case 69:
			eyeBlue+=0.1;
			break;
			case 82:
			eyeBlue-=0.1;
			break;*/
			}
			}, false);
			
			
}






// Add the event listeners for mousedown, mousemove, and mouseup



/*window.addEventListener('mouseup', e => {
  if (isDrawing === true) {
    //drawLine(context, x, y, e.offsetX, e.offsetY);
    x = 0;
    y = 0;
    isDrawing = false;
  }
});*/


/*
window.addEventListener('keydown', function(event) {
  //alert(event.keyCode);
  switch (event.keyCode) {
	case 77:
	if(mode==2) mode = 0;
	else mode=+1;
	break;
  }
}, false);

*/