%define major	2
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Name:		nifti
Summary:	Read and write files in the nifti-1 data format
Version:	2.0.0
Release:	%mkrel 2
License:	Public domain
Group:		Sciences/Other
Source0:	http://sourceforge.net/projects/niftilib/files/nifticlib/nifticlib_2_0_0/nifticlib-2.0.0.tar.gz
Url:		http://niftilib.sourceforge.net
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	cmake
BuildRequires:	itk-devel
BuildRequires:	zlib-devel

Patch0:		nifticlib-2.0.0-cmake.patch
Patch1:		nifticlib-2.0.0-underlink.patch
Patch2:		nifticlib-2.0.0-libdir.patch

%description
Niftilib is a set of i/o libraries for reading and writing files in the
nifti-1 data format. nifti-1 is a binary file format for storing medical
image data, e.g. magnetic resonance image (MRI) and functional MRI (fMRI)
brain images.

%files
%defattr(-,root,root)
%{_bindir}/*

#-----------------------------------------------------------------------
%package	-n %{libname}
Summary:	Read and write files in the nifti-1 data format
Group:		System/Libraries
Provides:	lib%{name} = %{version}-%{release}

%description	-n %{libname}
Niftilib is a set of i/o libraries for reading and writing files in the
nifti-1 data format. nifti-1 is a binary file format for storing medical
image data, e.g. magnetic resonance image (MRI) and functional MRI (fMRI)
brain images.

%files	-n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

#-----------------------------------------------------------------------
%package	-n %{devname}
Summary:	Read and write files in the nifti-1 data format
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description	-n %{devname}
Niftilib is a set of i/o libraries for reading and writing files in the
nifti-1 data format. nifti-1 is a binary file format for storing medical
image data, e.g. magnetic resonance image (MRI) and functional MRI (fMRI)
brain images.

%files	-n %{devname}
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so

#-----------------------------------------------------------------------
%prep
%setup -q -n %{name}clib-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%cmake \
	-DNIFTI_INSTALL_LIB_DIR:PATH=%{_libdir}
%make

%install
%makeinstall_std -C build

%clean
rm -rf %{buildroot}
