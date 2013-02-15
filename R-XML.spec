%global packname  XML
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          3.95.0.1
Release:          1
Summary:          Tools for parsing and generating XML within R and S-Plus
Group:            Sciences/Mathematics
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/XML_3.95-0.1.tar.gz
Requires:         R-methods R-utils 
Requires:         R-methods 
Requires:         R-bitops 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-utils
BuildRequires:    R-methods 
BuildRequires:    R-bitops 
BuildRequires:    libxml2-devel

%description
This package provides many approaches for both reading and creating XML
(and HTML) documents (including DTDs), both local and accessible via HTTP
or FTP.  It also offers access to an XPath "interpreter".

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
#%doc %{rlibdir}/%{packname}/Docs
#%doc %{rlibdir}/%{packname}/README*
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/exampleData
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/scripts


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.9_4-1
+ Revision: 775395
- Import R-XML
- Import R-XML


