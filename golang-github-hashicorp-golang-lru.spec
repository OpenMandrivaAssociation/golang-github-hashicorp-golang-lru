# http://github.com/hashicorp/golang-lru
%global goipath     github.com/hashicorp/golang-lru
%global commit      0fb14efe8c47ae851c0034ed7a448854d3d34cf3

%global common_description %{expand:
This provides the lru package which implements a fixed-size thread safe LRU 
cache. It is based on the cache in Groupcache.}

%gometa

Name:           golang-github-hashicorp-golang-lru
Version:        0
Release:        0.15%{?dist}
Summary:        Golang LRU cache
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{gobaseipath} prefix.


%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.git0fb14ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.14.git0fb14ef
- Upload glide files

* Fri Apr 13 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.13.20180413git0fb14ef
- Bump to upstream 0fb14efe8c47ae851c0034ed7a448854d3d34cf3

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.20151028gita6091bb
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gita6091bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gita6091bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gita6091bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gita6091bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.gita6091bb
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.gita6091bb
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gita6091bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.4.gita6091bb
- Bump to upstream a6091bb5d00e2e9c4a16a0e739e306f8a3071a3c
  related: #1250464

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.gitd85392d
- Update to spec-2.1
  related: #1250464

* Wed Aug 05 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.gitd85392d
- Update spec file to spec-2.0
  resolves: #1250464

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitd85392d
- First package for Fedora
  resolves: #1212048

