! Fortran 90 code used in the Bayesian estimation of GLMs
! Copyright (C) 2012  Chris Strickland

! This program is free software: you can redistribute it and/or modify
! it under the terms of the GNU General Public License as published by
! the Free Software Foundation, either version 3 of the License, or
! (at your option) any later version.

! This program is distributed in the hope that it will be useful,
! but WITHOUT ANY WARRANTY; without even the implied warranty of
! MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
! GNU General Public License for more details.

! You should have received a copy of the GNU General Public License
! along with this program.  If not, see <http://www.gnu.org/licenses/>.


! File is fortran code to assist in the estimation of the generalised
! linear model.

!Fortran 90 code used in auxiliary mixture algorithm
!for binomial logit model.

!Fortran code to sample indicators
subroutine sample_ind(srvec, randu, svec, prvec, lweight, ptr, ystar, llamb, &
        n, nsw, np)
    implicit none

    !input parameters
    integer, intent(in) :: n, nsw, np
    integer, intent(in), dimension(np) :: ptr
    real(kind = 8), intent(inout), dimension(n) :: srvec
    real(kind = 8), intent(in), dimension(n) :: ystar, randu, llamb
    real(kind = 8), intent(in), dimension(nsw) :: svec, lweight
    real(kind = 8), dimension(5) :: prvec

    !local variables
    integer :: i, j, ncomp, st, en, sample_sr, l
    real(kind = 8) :: ressq

!$omp parallel default(shared) private(i,st,en,ncomp,l,j,ressq,prvec)
!$omp do schedule(static)
    do i=1,n
        st = ptr(i)
        en = ptr(i + 1) - 1
        !number of components
        ncomp = en - st + 1
        l = 1
        do j = st, en
            ressq = ((ystar(i) -  llamb(i)) / svec(j)) ** 2
            prvec(l) = lweight(j) - log(svec(j)) -0.5 * ressq
            l = l + 1
        enddo

        j = sample_sr(prvec(1:ncomp), randu(i), ncomp)
        srvec(i) = svec(j)
    enddo
!$omp end do
!$omp end parallel
    
end subroutine sample_ind

!Fortran function to sample component of srvec
integer function sample_sr(prvec, randu, np)
    implicit none
    !input parameters
    integer, intent(in) :: np
    real(kind = 8), intent(in) :: randu
    real(kind = 8), dimension(np) :: prvec

    !local variables 
    integer :: i
    real(kind = 8) :: cumpr, sumpr, maxpr

    !normalise probabilties
    maxpr = maxval(prvec)
    sumpr = log(sum(exp(prvec - maxpr))) + maxpr
    prvec = prvec - sumpr

    !sample from probability mass function
    i = 1
    cumpr = exp(prvec(i))
    do while (randu > cumpr)
        i = i + 1
        cumpr = cumpr + exp(prvec(i))
    enddo

    !select ith component
    sample_sr = i
    return
end function sample_sr


