-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 13-11-2024 a las 04:57:52
-- Versión del servidor: 8.0.17
-- Versión de PHP: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gestion_empleados`
--
CREATE DATABASE IF NOT EXISTS `gestion_empleados` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `gestion_empleados`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamento`
--

CREATE TABLE `departamento` (
  `idDepartamento` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `gerente` varchar(45) DEFAULT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
  `idEmpleado` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `direccion` varchar(45) DEFAULT NULL,
  `telefono` varchar(45) DEFAULT NULL,
  `correo` varchar(45) NOT NULL,
  `fechaInicioContrato` date DEFAULT NULL,
  `salario` int(11) NOT NULL,
  `Departamento_idDepartamento` int(11) DEFAULT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`idEmpleado`, `nombre`, `direccion`, `telefono`, `correo`, `fechaInicioContrato`, `salario`, `Departamento_idDepartamento`, `Usuario_idUsuario`) VALUES
(1, 'izcan', 'chillan', '30309090', 'izcan@gmail.com', '2024-10-21', 500000, 1, 1),


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informe`
--

CREATE TABLE `informe` (
  `idInforme` int(11) NOT NULL,
  `contenido` varchar(250) NOT NULL,
  `Empleado_idEmpleado` int(11) NOT NULL,
  `fechaEmision` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `informe`
--

INSERT INTO `informe` (`idInforme`, `contenido`, `Empleado_idEmpleado`, `fechaEmision`) VALUES
(2, 'esto es un texto de ejemplo solo para probar que el programa es correcto y la libreria para el texto tambien lo es', 1, '2024-10-20 03:10:19'),
(3, 'esto es una prueba de creacion de informe con el implemento de try y except para la verificacion de que el usuario actual esta asociado con un empleado', 1, '2024-10-21 03:50:59');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto`
--

CREATE TABLE `proyecto` (
  `idProyecto` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `descripcion` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `fechaInicio` date DEFAULT NULL,
  `actividad` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `proyecto`
--

INSERT INTO `proyecto` (`idProyecto`, `nombre`, `descripcion`, `fechaInicio`, `actividad`) VALUES
(1, 'gestion de empleados', 'crear un sistema de gestion de empleados', '2024-10-16', 0),
(2, 'nombreproyecto', 'descripcionproyecto', '2024-02-01', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto_has_empleado`
--

CREATE TABLE `proyecto_has_empleado` (
  `Proyecto_idProyecto` int(11) NOT NULL,
  `Empleado_idEmpleado` int(11) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `proyecto_has_empleado`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_indicador`
--

CREATE TABLE `registro_indicador` (
  `idRegistroIndicador` int(11) NOT NULL,
  `nombre` varchar(10) NOT NULL,
  `fechaValor` date NOT NULL,
  `fechaConsulta` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Usuario_idUsuario` int(11) NOT NULL,
  `autor` varchar(25) NOT NULL,
  `valor` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `registro_indicador`
--

INSERT INTO `registro_indicador` (`idRegistroIndicador`, `nombre`, `fechaValor`, `fechaConsulta`, `Usuario_idUsuario`, `autor`, `valor`) VALUES
(1, 'dolar', '2024-11-05', '2024-11-06 02:55:07', 14, 'Mindicador.cl', 956.54),
(6, 'dolar', '2024-11-04', '2024-11-08 23:47:02', 14, 'Mindicador.cl', 961.29),
(7, 'dolar', '2024-11-05', '2024-11-08 23:47:02', 14, 'Mindicador.cl', 956.54),
(8, 'dolar', '2024-11-06', '2024-11-08 23:47:02', 14, 'Mindicador.cl', 954.9),
(9, 'dolar', '2024-11-07', '2024-11-08 23:47:02', 14, 'Mindicador.cl', 968.6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_tiempo`
--

CREATE TABLE `registro_tiempo` (
  `idRegistroTiempo` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `horasTrabajadas` int(11) DEFAULT NULL,
  `tareasRealizadas` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Empleado_idEmpleado` int(11) DEFAULT NULL,
  `Proyecto_idProyecto` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `registro_tiempo`
--

INSERT INTO `registro_tiempo` (`idRegistroTiempo`, `fecha`, `horasTrabajadas`, `tareasRealizadas`, `Empleado_idEmpleado`, `Proyecto_idProyecto`) VALUES
(2, '2024-10-19', 20, 'programa completo de gestion de empleados', 10, 3),
(3, '2024-05-12', 5, 'iterfaces mejoradas', 10, 3),
(4, '2024-05-23', 1, '', 10, 3),
(5, '2024-01-01', 20, 'si', 13, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `idRol` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`idRol`, `nombre`) VALUES
(1, 'empleado'),
(2, 'admin'),
(3, 'gerente'),
(4, 'recursos humanos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `idUsuario` int(11) NOT NULL,
  `nombreUsuario` varchar(45) DEFAULT NULL,
  `contraseña` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Rol_idRol` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`idUsuario`, `nombreUsuario`, `contraseña`, `Rol_idRol`) VALUES
(1, 'izcan', '123', 1),


--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`idDepartamento`);

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`idEmpleado`),
  ADD KEY `Departamento_idDepartamento` (`Departamento_idDepartamento`),
  ADD KEY `Usuario_idUsuario` (`Usuario_idUsuario`);

--
-- Indices de la tabla `informe`
--
ALTER TABLE `informe`
  ADD PRIMARY KEY (`idInforme`),
  ADD KEY `Empleado_idEmpleado` (`Empleado_idEmpleado`);

--
-- Indices de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  ADD PRIMARY KEY (`idProyecto`);

--
-- Indices de la tabla `proyecto_has_empleado`
--
ALTER TABLE `proyecto_has_empleado`
  ADD PRIMARY KEY (`Proyecto_idProyecto`,`Empleado_idEmpleado`),
  ADD KEY `Empleado_idEmpleado` (`Empleado_idEmpleado`);

--
-- Indices de la tabla `registro_indicador`
--
ALTER TABLE `registro_indicador`
  ADD PRIMARY KEY (`idRegistroIndicador`),
  ADD KEY `Usuario_idUsuario` (`Usuario_idUsuario`);

--
-- Indices de la tabla `registro_tiempo`
--
ALTER TABLE `registro_tiempo`
  ADD PRIMARY KEY (`idRegistroTiempo`),
  ADD KEY `Empleado_idEmpleado` (`Empleado_idEmpleado`),
  ADD KEY `Proyecto_idProyecto` (`Proyecto_idProyecto`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`idRol`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`idUsuario`),
  ADD KEY `Rol_idRol` (`Rol_idRol`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `departamento`
--
ALTER TABLE `departamento`
  MODIFY `idDepartamento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `empleado`
--
ALTER TABLE `empleado`
  MODIFY `idEmpleado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `informe`
--
ALTER TABLE `informe`
  MODIFY `idInforme` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  MODIFY `idProyecto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `registro_indicador`
--
ALTER TABLE `registro_indicador`
  MODIFY `idRegistroIndicador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `registro_tiempo`
--
ALTER TABLE `registro_tiempo`
  MODIFY `idRegistroTiempo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `rol`
--
ALTER TABLE `rol`
  MODIFY `idRol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `idUsuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD CONSTRAINT `empleado_ibfk_1` FOREIGN KEY (`Departamento_idDepartamento`) REFERENCES `departamento` (`idDepartamento`),
  ADD CONSTRAINT `empleado_ibfk_2` FOREIGN KEY (`Usuario_idUsuario`) REFERENCES `usuario` (`idUsuario`);

--
-- Filtros para la tabla `informe`
--
ALTER TABLE `informe`
  ADD CONSTRAINT `informe_ibfk_1` FOREIGN KEY (`Empleado_idEmpleado`) REFERENCES `empleado` (`idEmpleado`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Filtros para la tabla `proyecto_has_empleado`
--
ALTER TABLE `proyecto_has_empleado`
  ADD CONSTRAINT `proyecto_has_empleado_ibfk_1` FOREIGN KEY (`Proyecto_idProyecto`) REFERENCES `proyecto` (`idProyecto`),
  ADD CONSTRAINT `proyecto_has_empleado_ibfk_2` FOREIGN KEY (`Empleado_idEmpleado`) REFERENCES `empleado` (`idEmpleado`);

--
-- Filtros para la tabla `registro_indicador`
--
ALTER TABLE `registro_indicador`
  ADD CONSTRAINT `registro_indicador_ibfk_1` FOREIGN KEY (`Usuario_idUsuario`) REFERENCES `usuario` (`idUsuario`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Filtros para la tabla `registro_tiempo`
--
ALTER TABLE `registro_tiempo`
  ADD CONSTRAINT `registro_tiempo_ibfk_1` FOREIGN KEY (`Empleado_idEmpleado`) REFERENCES `empleado` (`idEmpleado`),
  ADD CONSTRAINT `registro_tiempo_ibfk_2` FOREIGN KEY (`Proyecto_idProyecto`) REFERENCES `proyecto` (`idProyecto`);

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`Rol_idRol`) REFERENCES `rol` (`idRol`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
