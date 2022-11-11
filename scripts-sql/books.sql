-- IMPORTANTE
-- ALTER TABLE libro
-- ADD FOREIGN KEY (id_image) REFERENCES image(id_image); 

-- SET FOREIGN_KEY_CHECKS=0;


-- AUTOR
INSERT INTO autor (id_autor, nombre, ap_paterno, ap_materno, pais) VALUES (1, "Alan", "Beaulieu", "", "Estados Unidos");
INSERT INTO autor (id_autor, nombre, ap_paterno, ap_materno, pais) VALUES (2, "David", "Flanagan", "", "Estados Unidos");
INSERT INTO autor (id_autor, nombre, ap_paterno, ap_materno, pais) VALUES (3, "Jasmina", "Susak", "", "Estados Unidos");
INSERT INTO autor (id_autor, nombre, ap_paterno, ap_materno, pais) VALUES (4, "Boris", "Cherny", "", "Estados Unidos");
INSERT INTO autor (id_autor, nombre, ap_paterno, ap_materno, pais) VALUES (5, "Edgar", "Allan", "Poe", "Estados Unidos");
INSERT INTO autor (id_autor, nombre, ap_paterno, ap_materno, pais) VALUES (6, "Lucy", "Maud", "Montgomery", "Canadá");
INSERT INTO autor (id_autor, nombre, ap_paterno, ap_materno, pais) VALUES (7, "Julio", "Florencio", "Cortázar", "Bélgica");
INSERT INTO autor (id_autor, nombre, ap_paterno, ap_materno, pais) VALUES (8, "Stephen", "Edwin", "King", "Estados Unidos");
INSERT INTO autor (id_autor, nombre, ap_paterno, ap_materno, pais) VALUES (9, "Alex", "Banks", "", "Estados Unidos");
INSERT INTO autor (id_autor, nombre, ap_paterno, ap_materno, pais) VALUES (10, "Yuli", "Vasiliev", "", "Estados Unidos");
INSERT INTO autor (id_autor, nombre, ap_paterno, ap_materno, pais) VALUES (11, "Aurelio", "Baldor", "de la Vega", "Cuba");
INSERT INTO autor (id_autor, nombre, ap_paterno, ap_materno, pais) VALUES (12, "Hervé", "Tullet", "", "Francia");

-- EDITORIAL
INSERT INTO editorial (id_editorial, pais, nombre) VALUES (1, "Estados Unidos", "O'Reilly Media");
INSERT INTO editorial (id_editorial, pais, nombre) VALUES (2, "Estados Unidos", "Independently published");
INSERT INTO editorial (id_editorial, pais, nombre) VALUES (3, "México", "Editorial Alma");
INSERT INTO editorial (id_editorial, pais, nombre) VALUES (4, "Internacional", "Penguin Random House Grupo Editorial");
INSERT INTO editorial (id_editorial, pais, nombre) VALUES (5, "Estados Unidos", "No Starch Press");
INSERT INTO editorial (id_editorial, pais, nombre) VALUES (6, "Internacional", "Océano Travesía");

-- CATEGORIA
INSERT INTO categoria (id_categoria, nombre) VALUES (1, "Computadoras y Tecnología");
INSERT INTO categoria (id_categoria, nombre) VALUES (2, "Libros de Texto y Guías de Estudio");
INSERT INTO categoria (id_categoria, nombre) VALUES (3, "Dibujo y arte");
INSERT INTO categoria (id_categoria, nombre) VALUES (4, "Literatura y ficción");
INSERT INTO categoria (id_categoria, nombre) VALUES (5, "Educación y referencia");
INSERT INTO categoria (id_categoria, nombre) VALUES (6, "Infantil y juvenil");

-- IMAGE
INSERT INTO image (id_image, path) VALUES (7, "/images/books/1.jpg");
INSERT INTO image (id_image, path) VALUES (8, "/images/books/2.jpg");
INSERT INTO image (id_image, path) VALUES (9, "/images/books/3.jpg");
INSERT INTO image (id_image, path) VALUES (10, "/images/books/4.jpg");
INSERT INTO image (id_image, path) VALUES (11, "/images/books/5.jpg");
INSERT INTO image (id_image, path) VALUES (12, "/images/books/6.JPG");
INSERT INTO image (id_image, path) VALUES (13, "/images/books/7.jpg");
INSERT INTO image (id_image, path) VALUES (14, "/images/books/8.jpg");
INSERT INTO image (id_image, path) VALUES (15, "/images/books/9.png");
INSERT INTO image (id_image, path) VALUES (16, "/images/books/10.jpg");
INSERT INTO image (id_image, path) VALUES (17, "/images/books/11.jpg");
INSERT INTO image (id_image, path) VALUES (18, "/images/books/12.jpg");
INSERT INTO image (id_image, path) VALUES (19, "/images/books/13.jpg");

-- LIBRO
INSERT INTO libro (id_libro, num_paginas, anio, isbn_10, isbn_13, nombre, estado, resenia, precio, stock, id_autor, id_editorial, id_categoria, id_image) 
VALUES (1, 377, 2020, 1492057614, 9781492057611, "Learning SQL: Generate, Manipulate, and Retrieve Data", "N", "A medida que los datos llegan a su empresa, necesita ponerla a trabajar de inmediato, y SQL es la mejor herramienta para el trabajo. Con la última edición de esta guía introductoria, el autor Alan Beaulieu ayuda a los desarrolladores a ponerse al día con los fundamentos de SQL para escribir aplicaciones de base de datos, realizar tareas administrativas y generar informes. Encontrará nuevos capítulos sobre SQL y Big Data, funciones analíticas y trabajo con bases de datos muy grandes. Cada capítulo presenta una lección independiente sobre un concepto o técnica SQL clave utilizando numerosas ilustraciones y ejemplos anotados. Los ejercicios te permiten practicar las habilidades que aprendes. El conocimiento de SQL es imprescindible para interactuar con los datos. Con Learning SQL, descubrirá rápidamente cómo poner en funcionamiento el poder y la flexibilidad de este lenguaje.", 
753, 3, 1, 1, 1, 7);
INSERT INTO libro (id_libro, num_paginas, anio, isbn_10, isbn_13, nombre, estado, resenia, precio, stock, id_autor, id_editorial, id_categoria, id_image) 
VALUES (2, 704, 2020, 1491952024, 9781491952023, "Javascript: The Definitive Guide: Master the World's Most-Used Programming Language", "N", "JavaScript es el lenguaje de programación de la web y es utilizado por más desarrolladores de software hoy en día que cualquier otro lenguaje de programación. Durante casi 25 años este best seller ha sido la guía de referencia para los programadores de JavaScript. La séptima edición está completamente actualizada para cubrir la versión 2020 de JavaScript, y los nuevos capítulos cubren clases, módulos, iteradores, generadores, Promises, async/await y metaprogramación. Encontrarás un código de ejemplo iluminador y atractivo en todas partes. Este libro es para programadores que quieren aprender JavaScript y para desarrolladores web que quieren llevar su comprensión y dominio al siguiente nivel. Comienza explicando el propio lenguaje JavaScript, en detalle, desde abajo hacia arriba. Luego se basa en esa base para cubrir la plataforma web y Node.js.", 
832, 2, 2, 1, 2, 8);
INSERT INTO libro (id_libro, num_paginas, anio, isbn_10, isbn_13, nombre, estado, resenia, precio, stock, id_autor, id_editorial, id_categoria, id_image) 
VALUES (3, 168, 2019, 1098833325, 9781098833329, "Cómo Dibujar Rostros: Aprende a Dibujar Personas Desde Cero (Spanish Edition)", "U", "¡Aprende a dibujar retratos realistas proporcionales en este tutorial paso a paso y fácil de seguir! Aprenda de la experimentada artista y profesora de arte, Jasmina Susak, quien te guiará en el proceso de dibujo desde cero hasta el retrato final.No solo aprenderás a dibujar rasgos faciales y piel, sino también a peinar, todo en este tutorial altamente detallado.Este tutorial fue hecho para artistas intermedios, pero los principiantes también deberían intentarlo, ya que Jasmina ha compartido muchos consejos y sugerencias que te ayudarán a comprender las cosas más importantes en un estilo realista de dibujo.¡Toma este libro, mejora tus habilidades de dibujo y lleva tus retratos a un nivel avanzado!", 
294, 1, 3, 2, 3, 9);
INSERT INTO libro (id_libro, num_paginas, anio, isbn_10, isbn_13, nombre, estado, resenia, precio, stock, id_autor, id_editorial, id_categoria, id_image) 
VALUES (4, 324, 2019, 1492037656, 9781492037651, "Programming Typescript: Making Your JavaScript Applications Scale", "U", "Cualquier programador que trabaje con un lenguaje de escritura dinámica le dirá lo difícil que es escalar a más líneas de código y más ingenieros. Es por eso que Facebook, Google y Microsoft inventaron capas de tipo estático gradual para su código JavaScript y Python dinámicamente escrito. Este práctico libro te muestra cómo una de estas capas tipo, TypeScript, es única entre ellas: hace que la programación sea divertida con su potente sistema de tipo estático. Si eres un programador con experiencia en JavaScript intermedio, el autor Boris Cherny te enseñará cómo dominar el lenguaje TypeScript. Entenderá cómo TypeScript puede ayudarlo a eliminar errores en su código y permitirle escalar su código a través de más ingenieros de lo que podía antes.", 
706, 1, 4, 1, 1, 10);
INSERT INTO libro (id_libro, num_paginas, anio, isbn_10, isbn_13, nombre, estado, resenia, precio, stock, id_autor, id_editorial, id_categoria, id_image) 
VALUES (5, 240, 2020, 841743030, 9788417430306, "Las Aventuras de Arthur Gordon Pym", "N", "Edgar Allan Poe fue uno de los pioneros indiscutibles del cuento de terror y la ciencia ficción. No es exagerado afirmar que ningún otro autor ha ejercido tanta influencia y ha generado tantas corrientes literarias como Poe. Este título marca un punto y aparte en su obra por tratarse de la única novela que escribió. Lo que comienza como una fascinante hazaña marina, da paso a una estremecedora aventura fantástica y de terror que fue completada por autores de la talla de Julio Verne y H. P. Lovecraft. It's no exaggeration to call Edgar Allan Poe one of the pioneers of horror and science fiction writing, or to declare that no author has left a legacy like his. This book is unique as the only novel he ever wrote. What begins as a fascinating maritime adventure gives way to a spine-tingling adventure that would later be taken up by the likes of Jules Verne and HP Lovecraft.", 
388, 1, 5, 3, 2, 11);
INSERT INTO libro (id_libro, num_paginas, anio, isbn_10, isbn_13, nombre, estado, resenia, precio, stock, id_autor, id_editorial, id_categoria, id_image) 
VALUES (6, 192, 2021, 6073808305, 9786073808309, "Ana de las Tejas Verdes 1. La Llegada", "U", "UN CLÁSICO QUE VUELVE para ROBARNOS el CORAZÓN. La NOVELA QUE INSPIRÓ la SERIE de NETFLIX «ANNE with an E». Matthew y Marilla llevan una vida tranquila y rutinaria en el pequeño pueblo de Avonlea. Ya ancianos, deciden adoptar un huérfano para que los ayude con las tareas de la granja. Pero en vez del niño prometido por el orfanato, a casa de los Cuthbert llega Ana, una niña valiente y apasionada con una imaginación desbordante que conquistará a todo el mundo. «Hay un montón de Anas distintas dentro de mí. Algunas veces pienso que esa es la razón de que yo sea una persona tan cargante. Si fuera siempre una sola Ana, sería mucho más cómodo, pero también muchísimo menos interesante.».", 
199, 3, 6, 4, 4, 12);
INSERT INTO libro (id_libro, num_paginas, anio, isbn_10, isbn_13, nombre, estado, resenia, precio, stock, id_autor, id_editorial, id_categoria, id_image) 
VALUES (7, 224, 2022, 6073812191, 9786073812191, "Ana de las tejas verdes 4. Más aventuras en Avonlea", "U", "El amor está en el aire en Avonlea. Antiguos enamorados que se reencuentran, romances que no lo eran, nuevas parejas y algún encuentro mágico que provoca un buen entuerto... ¡Nunca faltan las emociones cuando Ana Shirley anda cerca! La soñadora pelirroja se hace mayor y la vida le reserva sus propias sorpresas.", 
199, 3, 6, 4, 4, 13);
INSERT INTO libro (id_libro, num_paginas, anio, isbn_10, isbn_13, nombre, estado, resenia, precio, stock, id_autor, id_editorial, id_categoria, id_image) 
VALUES (8, 192, 2019, 6073147759, 9786073147750, "Todos los fuegos el fuego", "N", "Los cuentos de Cortázar son ritos de humor, de parodia y de ternura, solicitudes de complicidad, invitaciones a la iniciación repentina.Todos los fuegos el fuego (1966) es una de las mejores recopilaciones de relatos que un lector puede leer. O algo más que leer: vivir como experiencia propia, que le ensanche las percepciones y le enriquezca la memoria. Un libro que ofrece ocho muestras rotundas de la plenitud creadora que alcanzan los cuentos de Cortázar.", 
166, 2, 7, 4, 4, 14);
INSERT INTO libro (id_libro, num_paginas, anio, isbn_10, isbn_13, nombre, estado, resenia, precio, stock, id_autor, id_editorial, id_categoria, id_image) 
VALUES (9, 856, 2022, 6073819447, 9786073819442, "Cuento de hadas", "N", "Charlie Reade parece un estudiante de instituto normal y corriente, pero carga con un gran peso sobre los hombros. Su madre fue víctima de un atropello cuando él tenía solo diez años y la pena empujó a su padre a la bebida. Aunque era demasiado joven, Charlie tuvo que aprender a cuidarse solo... y también a ocuparse de su padre. Ahora, con diecisiete años, Charlie encuentra dos amigos inesperados: una perra llamada Radar y Howard Bowditch, su anciano dueño. El señor Bowditch es un ermitaño que vive en una colina enorme, en una casa enorme que tiene un cobertizo cerrado a cal y canto en el patio trasero. A veces, sonidos extraños emergen de él. Mientras Charlie se encarga de hacer recados para el señor Bowditch, Radar y él se hacen inseparables. Cuando el anciano fallece, le deja al chico una cinta de casete que contiene una historia increíble y el gran secreto que Bowditch ha guardado durante toda su vida: dentro de su cobertizo existe un portal que conduce a otro mundo.", 
589, 2, 8, 4, 4, 15);
INSERT INTO libro (id_libro, num_paginas, anio, isbn_10, isbn_13, nombre, estado, resenia, precio, stock, id_autor, id_editorial, id_categoria, id_image) 
VALUES (10, 310, 2020, 1492051721, 9781492051725, "Learning React: Modern Patterns for Developing React Apps", "N", "Si desea aprender cómo construir aplicaciones eficientes de React, este es su libro. Ideal para desarrolladores web e ingenieros de software que entienden cómo JavaScript, CSS y HTML funcionan en el navegador, esta edición actualizada proporciona las mejores prácticas y patrones para escribir código React moderno. Ningún conocimiento previo de React o JavaScript funcional es necesario. Con su hoja de ruta de aprendizaje, los autores Alex Banks y Eve Porcello le muestran cómo crear IU que pueden mostrar hábilmente los cambios sin recargas de página en sitios web de gran escala y basados en datos. También descubrirá cómo trabajar con la programación funcional y las últimas funciones de ECMAScript. Una vez que aprenda cómo construir componentes de React con esta guía práctica, entenderá lo útil que puede ser React en su organización.", 
739, 2, 9, 1, 1, 16);
INSERT INTO libro (id_libro, num_paginas, anio, isbn_10, isbn_13, nombre, estado, resenia, precio, stock, id_autor, id_editorial, id_categoria, id_image) 
VALUES (11, 240, 2022, 1718502206, 9781718502208, "Python for Data Science: A Hands-On Introduction", "N", "Python es una opción ideal para acceder, manipular y obtener información de datos de todo tipo. Python for Data Science te introduce en el mundo Pythonic del análisis de datos con un enfoque de aprendizaje práctico basado en ejemplos prácticos y actividades prácticas. Aprenderá a escribir código Python para obtener, transformar y analizar datos, practicando técnicas de procesamiento de datos de última generación para casos de uso en administración de negocios, marketing y soporte de decisiones.", 
568, 2, 10, 5, 1, 17);
INSERT INTO libro (id_libro, num_paginas, anio, isbn_10, isbn_13, nombre, estado, resenia, precio, stock, id_autor, id_editorial, id_categoria, id_image) 
VALUES (12, 576, 2007, 9708170003, 9789708170000, "Álgebra Baldor", "U", "Esta segunda edición de Álgebra de Baldor está elaborada con un diseño moderno y atractivo en el que se incluyen gráficos e ilustraciones, así como un CD interactivo con videos acerca de aplicaciones del álgebra en la vida cotidiana y ejemplos paso a paso.", 
355, 15, 11, 6, 5, 18);
INSERT INTO libro (id_libro, num_paginas, anio, isbn_10, isbn_13, nombre, estado, resenia, precio, stock, id_autor, id_editorial, id_categoria, id_image) 
VALUES (13, 56, 2011, 6074003769, 9786074003765, "Un libro", "U", "En la actualidad la tecnología ocupa la atención de los pequeños. Este libro ayuda a despertar la sensibilidad, la inteligencia, la capacidad de análisis y acerca a los pequeños a las cosas sencillas, simples, de forma divertida. Un libro es mucho más que eso: un libro común. No es únicamente para leerse y hojearse, ¡es para divertirse! Los niños –y hasta los adultos, ¿por qué no?– deberán seguir las instrucciones que vienen en cada página para ver lo que pasa.", 
252, 10, 12, 6, 6, 19);
INSERT INTO libro (id_libro, num_paginas, anio, isbn_10, isbn_13, nombre, estado, resenia, precio, stock, id_autor, id_editorial, id_categoria, id_image) 
VALUES (11, 0, 0, 0, 0, "", "", "", 
0, 0, 0, 0, 0, 0);
