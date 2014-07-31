%global   real_name ffmpeg
Name:	     ffmpeg-xpra	
Version:     2.2.5
Release:     1%{?dist}
Summary:     ffmpeg libraries for xpra	

Group:       Applications/Multimedia
License:     GPL
URL:	     http://www.ffmpeg.org
Source0:     http://www.ffmpeg.org/releases/ffmpeg-%{version}.tar.bz2
BuildRoot:   %(mktemp -ud %{_tmppath}/%{real_name}-%{version}-%{release}-XXXXXX)

BuildRequires:	x264-xpra-devel
BuildRequires:	yasm


%if 0%{?fc19}
BuildRequires: perl-podlators
%endif

%description
ffmpeg libraries for xpra


%package devel
Summary:   Development package for %{real_name}
Group:     Development/libraries
Requires:  %{name} = %{version}-%{release}
Requires:  pkgconfig

%description devel
This package contains the development files for %{name}.


%prep
%setup -q -n %{real_name}-%{version}


%build
# set pkg_config_path for xpra video libs
./configure \
    --prefix="%{_prefix}" \
    --libdir="%{_libdir}/xpra" \
    --shlibdir="%{_libdir}/xpra" \
    --mandir="%{_mandir}" \
    --incdir="%{_includedir}/xpra" \
    --extra-cflags="-I%{_includedir}/xpra" \
    --extra-ldflags="-L%{_libdir}/xpra" \
    --enable-runtime-cpudetect \
    --disable-avdevice \
    --enable-pic \
    --disable-zlib \
    --disable-filters \
    --disable-everything \
    --disable-doc \
    --disable-programs \
    --enable-libx264 \
    --enable-libvpx \
    --enable-gpl \
    --enable-decoder=h264 \
    --enable-decoder=hevc \
    --enable-decoder=vp8 \
    --enable-decoder=vp9 \
    --enable-shared \
    --disable-symver
    #--enable-static \

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

#%post -p /sbin/ldconfig
#%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING* CREDITS README doc/ffserver.conf
%{_libdir}/xpra/libavcodec.so.*
%{_libdir}/xpra/libavfilter.so.*
%{_libdir}/xpra/libavformat.so.*
%{_libdir}/xpra/libavutil.so.*
%{_libdir}/xpra/libpostproc.so.*
%{_libdir}/xpra/libswresample.so.*
%{_libdir}/xpra/libswscale.so.*


%files devel
%doc MAINTAINERS doc/APIchanges
%defattr(-,root,root,-)
%{_includedir}/xpra/libavcodec/
%{_includedir}/xpra/libavfilter/
%{_includedir}/xpra/libavformat/
%{_includedir}/xpra/libavutil/
%{_includedir}/xpra/libpostproc/
%{_includedir}/xpra/libswresample/
%{_includedir}/xpra/libswscale/
%{_libdir}/xpra/libavcodec.a
%{_libdir}/xpra/libavfilter.a
%{_libdir}/xpra/libavformat.a
%{_libdir}/xpra/libavutil.a
%{_libdir}/xpra/libpostproc.a
%{_libdir}/xpra/libswresample.a
%{_libdir}/xpra/libswscale.a
%{_libdir}/xpra/libavcodec.so
%{_libdir}/xpra/libavfilter.so
%{_libdir}/xpra/libavformat.so
%{_libdir}/xpra/libavutil.so
%{_libdir}/xpra/libpostproc.so
%{_libdir}/xpra/libswresample.so
%{_libdir}/xpra/libswscale.so
%{_libdir}/xpra/pkgconfig/libavcodec.pc
%{_libdir}/xpra/pkgconfig/libavfilter.pc
%{_libdir}/xpra/pkgconfig/libavformat.pc
%{_libdir}/xpra/pkgconfig/libavutil.pc
%{_libdir}/xpra/pkgconfig/libpostproc.pc
%{_libdir}/xpra/pkgconfig/libswresample.pc
%{_libdir}/xpra/pkgconfig/libswscale.pc



%changelog
* Thu Jul 31 2014 Antoine Martin <antoine@devloop.org.uk> 2.2.5
- version bump

* Sun Jul 20 2014 Antoine Martin <antoine@devloop.org.uk> 2.2.4
- version bump

* Mon Jul 14 2014 Matthew Gyurgyik <pyther@pyther.net>
- initial package 
