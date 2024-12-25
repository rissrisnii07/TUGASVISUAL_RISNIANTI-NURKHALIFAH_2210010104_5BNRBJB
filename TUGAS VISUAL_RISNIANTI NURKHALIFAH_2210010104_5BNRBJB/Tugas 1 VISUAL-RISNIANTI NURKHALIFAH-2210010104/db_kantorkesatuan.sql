-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 16 Okt 2024 pada 07.14
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_kantorkesatuan`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_dokumentasi`
--

CREATE TABLE `tb_dokumentasi` (
  `id_dok` int(11) NOT NULL,
  `tgl_dok` date NOT NULL,
  `judul` varchar(225) NOT NULL,
  `foto` text NOT NULL,
  `isi` text NOT NULL,
  `link` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_jabatan`
--

CREATE TABLE `tb_jabatan` (
  `id_jabatan` int(11) NOT NULL,
  `kode_jabatan` varchar(50) NOT NULL,
  `nama_jabatan` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_klasifikasi`
--

CREATE TABLE `tb_klasifikasi` (
  `id_kls` int(11) NOT NULL,
  `kode_klasifikasi` varchar(50) NOT NULL,
  `nama_klasifikasi` varchar(250) NOT NULL,
  `uraian` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_leveluser`
--

CREATE TABLE `tb_leveluser` (
  `id_level_user` int(11) NOT NULL,
  `nama_level` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_slider`
--

CREATE TABLE `tb_slider` (
  `id_slider` int(11) NOT NULL,
  `gambar` text NOT NULL,
  `keterangan` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_suratkeluar`
--

CREATE TABLE `tb_suratkeluar` (
  `id_surat_keluar` int(11) NOT NULL,
  `no_agenda` varchar(225) NOT NULL,
  `no_surat` varchar(225) NOT NULL,
  `klasifikasi` int(11) NOT NULL,
  `sifat` varchar(225) NOT NULL,
  `tanggal_surat` date NOT NULL,
  `tanggal_masuk` date NOT NULL,
  `perihal` text NOT NULL,
  `retensi` varchar(50) NOT NULL,
  `kepada` text NOT NULL,
  `foto` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_suratmasuk`
--

CREATE TABLE `tb_suratmasuk` (
  `id_surat_masuk` int(11) NOT NULL,
  `no_surat` varchar(50) NOT NULL,
  `klasifikasi` int(11) NOT NULL,
  `sifat` varchar(225) NOT NULL,
  `tanggal_surat` date NOT NULL,
  `tanggal_masuk` date NOT NULL,
  `perihal` text NOT NULL,
  `retensi` varchar(50) NOT NULL,
  `pengirim` text NOT NULL,
  `kepada` text NOT NULL,
  `foto` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_user`
--

CREATE TABLE `tb_user` (
  `id_user` int(11) NOT NULL,
  `nama_lengkap` varchar(225) NOT NULL,
  `nip` varchar(50) NOT NULL,
  `username` varchar(225) NOT NULL,
  `password` varchar(225) NOT NULL,
  `id_jabatan` int(11) NOT NULL,
  `id_level_user` int(11) NOT NULL,
  `foto` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `tb_dokumentasi`
--
ALTER TABLE `tb_dokumentasi`
  ADD PRIMARY KEY (`id_dok`),
  ADD UNIQUE KEY `isi` (`isi`) USING HASH;

--
-- Indeks untuk tabel `tb_jabatan`
--
ALTER TABLE `tb_jabatan`
  ADD PRIMARY KEY (`id_jabatan`);

--
-- Indeks untuk tabel `tb_klasifikasi`
--
ALTER TABLE `tb_klasifikasi`
  ADD PRIMARY KEY (`id_kls`);

--
-- Indeks untuk tabel `tb_leveluser`
--
ALTER TABLE `tb_leveluser`
  ADD PRIMARY KEY (`id_level_user`),
  ADD KEY `nama_level` (`nama_level`);

--
-- Indeks untuk tabel `tb_slider`
--
ALTER TABLE `tb_slider`
  ADD PRIMARY KEY (`id_slider`);

--
-- Indeks untuk tabel `tb_suratkeluar`
--
ALTER TABLE `tb_suratkeluar`
  ADD PRIMARY KEY (`id_surat_keluar`),
  ADD UNIQUE KEY `klasifikasi` (`klasifikasi`);

--
-- Indeks untuk tabel `tb_suratmasuk`
--
ALTER TABLE `tb_suratmasuk`
  ADD PRIMARY KEY (`id_surat_masuk`),
  ADD UNIQUE KEY `klasifikasi` (`klasifikasi`);

--
-- Indeks untuk tabel `tb_user`
--
ALTER TABLE `tb_user`
  ADD PRIMARY KEY (`id_user`),
  ADD UNIQUE KEY `id_jabatan` (`id_jabatan`),
  ADD UNIQUE KEY `id_level_user` (`id_level_user`);

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `tb_dokumentasi`
--
ALTER TABLE `tb_dokumentasi`
  ADD CONSTRAINT `tb_dokumentasi_ibfk_1` FOREIGN KEY (`id_dok`) REFERENCES `tb_slider` (`id_slider`);

--
-- Ketidakleluasaan untuk tabel `tb_klasifikasi`
--
ALTER TABLE `tb_klasifikasi`
  ADD CONSTRAINT `tb_klasifikasi_ibfk_1` FOREIGN KEY (`id_kls`) REFERENCES `tb_suratkeluar` (`id_surat_keluar`);

--
-- Ketidakleluasaan untuk tabel `tb_suratmasuk`
--
ALTER TABLE `tb_suratmasuk`
  ADD CONSTRAINT `tb_suratmasuk_ibfk_1` FOREIGN KEY (`klasifikasi`) REFERENCES `tb_klasifikasi` (`id_kls`);

--
-- Ketidakleluasaan untuk tabel `tb_user`
--
ALTER TABLE `tb_user`
  ADD CONSTRAINT `tb_user_ibfk_1` FOREIGN KEY (`id_jabatan`) REFERENCES `tb_jabatan` (`id_jabatan`),
  ADD CONSTRAINT `tb_user_ibfk_2` FOREIGN KEY (`id_level_user`) REFERENCES `tb_leveluser` (`id_level_user`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
