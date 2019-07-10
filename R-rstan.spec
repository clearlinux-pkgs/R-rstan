#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rstan
Version  : 2.19.2
Release  : 28
URL      : https://cran.r-project.org/src/contrib/rstan_2.19.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rstan_2.19.2.tar.gz
Summary  : R Interface to Stan
Group    : Development/Tools
License  : GPL-3.0
Requires: R-rstan-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-StanHeaders
Requires: R-ggplot2
Requires: R-gridExtra
Requires: R-inline
Requires: R-loo
Requires: R-pkgbuild
BuildRequires : R-BH
BuildRequires : R-Rcpp
BuildRequires : R-RcppEigen
BuildRequires : R-StanHeaders
BuildRequires : R-coda
BuildRequires : R-ggplot2
BuildRequires : R-gridExtra
BuildRequires : R-inline
BuildRequires : R-loo
BuildRequires : R-pkgbuild
BuildRequires : buildreq-R

%description
estimate, and analyze Stan models by accessing the header-only Stan library
    provided by the 'StanHeaders' package. The Stan project develops a probabilistic
    programming language that implements full Bayesian statistical inference
    via Markov Chain Monte Carlo, rough Bayesian inference via 'variational'
    approximation, and (optionally penalized) maximum likelihood estimation via
    optimization. In all three cases, automatic differentiation is used to quickly
    and accurately evaluate gradients without burdening the user with the need to
    derive the partial derivatives.

%package lib
Summary: lib components for the R-rstan package.
Group: Libraries

%description lib
lib components for the R-rstan package.


%prep
%setup -q -c -n rstan

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1562775278

%install
export SOURCE_DATE_EPOCH=1562775278
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rstan
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rstan
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rstan
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rstan || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rstan/CITATION
/usr/lib64/R/library/rstan/DESCRIPTION
/usr/lib64/R/library/rstan/INDEX
/usr/lib64/R/library/rstan/Meta/Rd.rds
/usr/lib64/R/library/rstan/Meta/features.rds
/usr/lib64/R/library/rstan/Meta/hsearch.rds
/usr/lib64/R/library/rstan/Meta/links.rds
/usr/lib64/R/library/rstan/Meta/nsInfo.rds
/usr/lib64/R/library/rstan/Meta/package.rds
/usr/lib64/R/library/rstan/Meta/vignette.rds
/usr/lib64/R/library/rstan/NAMESPACE
/usr/lib64/R/library/rstan/NEWS
/usr/lib64/R/library/rstan/R/rstan
/usr/lib64/R/library/rstan/R/rstan.rdb
/usr/lib64/R/library/rstan/R/rstan.rdx
/usr/lib64/R/library/rstan/R/sysdata.rdb
/usr/lib64/R/library/rstan/R/sysdata.rdx
/usr/lib64/R/library/rstan/doc/SBC.R
/usr/lib64/R/library/rstan/doc/SBC.Rmd
/usr/lib64/R/library/rstan/doc/SBC.html
/usr/lib64/R/library/rstan/doc/external.R
/usr/lib64/R/library/rstan/doc/external.Rmd
/usr/lib64/R/library/rstan/doc/external.html
/usr/lib64/R/library/rstan/doc/fib.hpp
/usr/lib64/R/library/rstan/doc/index.html
/usr/lib64/R/library/rstan/doc/rstan.R
/usr/lib64/R/library/rstan/doc/rstan.Rmd
/usr/lib64/R/library/rstan/doc/rstan.bib
/usr/lib64/R/library/rstan/doc/rstan.html
/usr/lib64/R/library/rstan/doc/schools.stan
/usr/lib64/R/library/rstan/doc/sinc.hpp
/usr/lib64/R/library/rstan/doc/stanfit-objects.R
/usr/lib64/R/library/rstan/doc/stanfit-objects.Rmd
/usr/lib64/R/library/rstan/doc/stanfit-objects.html
/usr/lib64/R/library/rstan/help/AnIndex
/usr/lib64/R/library/rstan/help/aliases.rds
/usr/lib64/R/library/rstan/help/figures/stanlogo.png
/usr/lib64/R/library/rstan/help/paths.rds
/usr/lib64/R/library/rstan/help/rstan.rdb
/usr/lib64/R/library/rstan/help/rstan.rdx
/usr/lib64/R/library/rstan/html/00Index.html
/usr/lib64/R/library/rstan/html/R.css
/usr/lib64/R/library/rstan/include/exporter.h
/usr/lib64/R/library/rstan/include/rstan/boost_random_R.hpp
/usr/lib64/R/library/rstan/include/rstan/comment_writer.hpp
/usr/lib64/R/library/rstan/include/rstan/filtered_values.hpp
/usr/lib64/R/library/rstan/include/rstan/io/r_ostream.hpp
/usr/lib64/R/library/rstan/include/rstan/io/rlist_ref_var_context.hpp
/usr/lib64/R/library/rstan/include/rstan/logger.hpp
/usr/lib64/R/library/rstan/include/rstan/rcpp_module_def_for_rstan.hpp
/usr/lib64/R/library/rstan/include/rstan/rstan_writer.hpp
/usr/lib64/R/library/rstan/include/rstan/rstaninc.hpp
/usr/lib64/R/library/rstan/include/rstan/stan_args.hpp
/usr/lib64/R/library/rstan/include/rstan/stan_fit.hpp
/usr/lib64/R/library/rstan/include/rstan/sum_values.hpp
/usr/lib64/R/library/rstan/include/rstan/value.hpp
/usr/lib64/R/library/rstan/include/rstan/values.hpp
/usr/lib64/R/library/rstan/misc/rstan_doc_ex_1.csv
/usr/lib64/R/library/rstan/misc/rstan_doc_ex_2.csv
/usr/lib64/R/library/rstan/misc/rstan_doc_ex_3.csv
/usr/lib64/R/library/rstan/misc/rstan_doc_ex_4.csv
/usr/lib64/R/library/rstan/misc/rstan_doc_ex_incomplete_1.csv
/usr/lib64/R/library/rstan/misc/rstan_doc_ex_incomplete_2.csv
/usr/lib64/R/library/rstan/misc/stan_progress.html
/usr/lib64/R/library/rstan/tests/doRUnit.R
/usr/lib64/R/library/rstan/unitTests/runRunitTests.R
/usr/lib64/R/library/rstan/unitTests/runit.test.chains.R
/usr/lib64/R/library/rstan/unitTests/runit.test.extract_sparse_parts.R
/usr/lib64/R/library/rstan/unitTests/runit.test.misc.R
/usr/lib64/R/library/rstan/unitTests/runit.test.options.R
/usr/lib64/R/library/rstan/unitTests/runit.test.stan_csv.R
/usr/lib64/R/library/rstan/unitTests/test_r_ostream.R
/usr/lib64/R/library/rstan/unitTests/test_rlist_ref_var_context.R
/usr/lib64/R/library/rstan/unitTests/test_rlist_ref_var_context.cpp
/usr/lib64/R/library/rstan/unitTests/testdata/blocker1.csv
/usr/lib64/R/library/rstan/unitTests/testdata/blocker2.csv

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rstan/libs/rstan.so
