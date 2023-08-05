c Modified by Chris Strickland 2012 for use with Python and Numpy's
c random number generator
c
c  A C-program for MT19937, with initialization improved 2002/1/26.
c  Coded by Takuji Nishimura and Makoto Matsumoto.
c
c  Before using, initialize the state by using init_genrand(seed)  
c  or init_by_array(init_key, key_length).
c
c  Copyright (C) 1997 - 2002, Makoto Matsumoto and Takuji Nishimura,
c  All rights reserved.                          
c  Copyright (C) 2005, Mutsuo Saito,
c  All rights reserved.                          
c
c  Redistribution and use in source and binary forms, with or without
c  modification, are permitted provided that the following conditions
c  are met:
c
c    1. Redistributions of source code must retain the above copyright
c       notice, this list of conditions and the following disclaimer.
c
c    2. Redistributions in binary form must reproduce the above copyright
c       notice, this list of conditions and the following disclaimer in the
c       documentation and/or other materials provided with the distribution.
c
c    3. The names of its contributors may not be used to endorse or promote 
c       products derived from this software without specific prior written 
c       permission.
c
c  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
c  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
c  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
c  A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
c  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
c  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
c  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
c  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
c  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
c  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
c  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
c
c
c  Any feedback is very welcome.
c  http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html
c  email: m-mat @ math.sci.hiroshima-u.ac.jp (remove space)
c
c-----------------------------------------------------------------------
c  FORTRAN77 translation by Tsuyoshi TADA. (2005/12/19)
c
c     ---------- initialize routines ----------
c  subroutine init_genrand(seed): initialize with a seed
c  subroutine init_by_array(init_key,key_length): initialize by an array
c
c     ---------- generate functions ----------
c  integer function genrand_int32(): signed 32-bit integer
c  integer function genrand_int31(): unsigned 31-bit integer
c  double precision function genrand_real1(): [0,1] with 32-bit resolution
c  double precision function genrand_real2(): [0,1) with 32-bit resolution
c  double precision function genrand_real3(): (0,1) with 32-bit resolution
c  double precision function genrand_res53(): (0,1) with 53-bit resolution
c
c  This program uses the following non-standard intrinsics.
c    ishft(i,n): If n>0, shifts bits in i by n positions to left.
c                If n<0, shifts bits in i by n positions to right.
c    iand (i,j): Performs logical AND on corresponding bits of i and j.
c    ior  (i,j): Performs inclusive OR on corresponding bits of i and j.
c    ieor (i,j): Performs exclusive OR on corresponding bits of i and j.
c
c-----------------------------------------------------------------------
c     generates a random number on [0,0xffffffff]-interval
c-----------------------------------------------------------------------

      integer function genrand_int32(mt,mag01,argv)
c     argv(1) = mti
c     argv(2) = UPPER_MASK
c     argv(3) = LOWER_MASK
c     argv[4] = T1_MASK
c     argv[5] = T2_MASK

      integer N,M
      parameter (N=624)
      parameter (M=397)
      integer mt(0:N-1)
      integer y,kk, argv(6)
      integer mag01(0:1)


      if(argv(1).ge.N)then
        do 100 kk=0,N-M-1
          y=ior(iand(mt(kk),argv(2)),iand(mt(kk+1),argv(3)))
          mt(kk)=ieor(ieor(mt(kk+M),ishft(y,-1)),mag01(iand(y,1)))
  100   continue
        do 200 kk=N-M,N-1-1
          y=ior(iand(mt(kk),argv(2)),iand(mt(kk+1),argv(3)))
          mt(kk)=ieor(ieor(mt(kk+(M-N)),ishft(y,-1)),mag01(iand(y,1)))
  200   continue
        y=ior(iand(mt(N-1),argv(2)),iand(mt(0),argv(3)))
        mt(kk)=ieor(ieor(mt(M-1),ishft(y,-1)),mag01(iand(y,1)))
        argv(1)=0
      endif
c
      y=mt(argv(1))
      argv(1)=argv(1)+1
c
      y=ieor(y,ishft(y,-11))
      y=ieor(y,iand(ishft(y,7),argv(4)))
      y=ieor(y,iand(ishft(y,15),argv(5)))
      y=ieor(y,ishft(y,-18))
c
      genrand_int32=y
      return
      end

c-----------------------------------------------------------------------
c     fills array with uniform random numbers      
c-----------------------------------------------------------------------
      subroutine randv(rndv, mt, mag01, argv, n)
      implicit none
      integer mt(624),mag01(2),argv(6), n, i
      real*8 rndv(n), genrand_res53
      
cf2py intent(inout) rndv
cf2py intent(inout) mt
cf2py intent(inout) mag0
cf2py intent(inout) argv


      do i=1,n
          rndv(i)=genrand_res53(mt,mag01,argv)
      enddo
      end subroutine randv

      subroutine randm(rndm, mt, mag01, argv, n, m)
      implicit none
      integer n,m
      integer mt(624),mag01(2),argv(6), i, j
      real*8 rndm(n,m), genrand_res53

cf2py intent(inout) rndm
cf2py intent(inout) mt
cf2py intent(inout) mag0
cf2py intent(inout) argv

      do i=1,n
          do j=1,m
              rndm(i,j)=genrand_res53(mt,mag01,argv)
          enddo
      enddo
      end subroutine randm

      subroutine randa3d(rnda, mt, mag01, argv, n, m,r)
      implicit none
      integer n,m,r
      integer mt(624),mag01(2),argv(6), i, j, k
      real*8 rnda(n,m,r), genrand_res53

cf2py intent(inout) rnda
cf2py intent(inout) mt
cf2py intent(inout) mag0
cf2py intent(inout) argv
      do i=1,n
          do j=1,m
              do k=1,r
                  rnda(i,j, k)=genrand_res53(mt,mag01,argv)
              enddo
          enddo
      enddo
      end subroutine randa3d
      
c-----------------------------------------------------------------------
c     generates a random number from exponential (1)
c-----------------------------------------------------------------------

      real*8 function rand_exp(mt, mag01, argv)
      implicit none
      integer mt(624),mag01(2),argv(6)
      real*8 genrand_res53

      rand_exp = -log(genrand_res53(mt,mag01, argv))
      return
      end function rand_exp

      subroutine randv_exp(rndv, mt, mag01, argv, n)
      implicit none
      integer mt(624),mag01(2),argv(6), n, i
      real*8 rndv(n), genrand_res53
      
cf2py intent(inout) rndv
cf2py intent(inout) mt
cf2py intent(inout) mag0
cf2py intent(inout) argv


      do i=1,n
          rndv(i)=-log(genrand_res53(mt,mag01,argv))
      enddo
      end subroutine randv_exp

      subroutine randm_exp(rndm, mt, mag01, argv, n, m)
      implicit none
      integer n,m
      integer mt(624),mag01(2),argv(6), i, j
      real*8 rndm(n,m), genrand_res53

cf2py intent(inout) rndm
cf2py intent(inout) mt
cf2py intent(inout) mag0
cf2py intent(inout) argv

      do i=1,n
          do j=1,m
              rndm(i,j)=-log(genrand_res53(mt,mag01,argv))
          enddo
      enddo
      end subroutine

      subroutine randa3d_exp(rnda, mt, mag01, argv, n, m,r)
      implicit none
      integer n,m,r
      integer mt(624),mag01(2),argv(6), i, j, k
      real*8 rnda(n,m,r), genrand_res53

cf2py intent(inout) rnda
cf2py intent(inout) mt
cf2py intent(inout) mag0
cf2py intent(inout) argv
      do i=1,n
          do j=1,m
              do k=1,r
                  rnda(i,j, k)=-log(genrand_res53(mt,mag01,argv))
              enddo
          enddo
      enddo
      end subroutine randa3d_exp


c-----------------------------------------------------------------------
c     generates a random number from a truncated standard normal
c     distribution with a lowerbound of a and an upperbound of b   
c----------------------------------------------------------------------

      real*8 function tnorm(a,b,mt,mag01,argv,cached)
      implicit none
      integer mt(624),mag01(2),argv(6)
      real*8 a,b,ta,tb
      real*8 t1,t2,t3,t4,pnorm, mult
      real*8 ratio, cached(1), norm_r, exp_r
      real*8 argmax, uni_r, hnorm_r

      parameter(t1=0.150)
      parameter(t2=2.18)
      parameter(t3=0.725)
      parameter(t4=0.45)
      ta = a
      tb = b

      if (ta.lt.-15.0.and.tb.gt.15.0) then
          !normal rejection sampling
          !print*, "nrs", ta, tb
          tnorm = norm_r(a,b,mt,mag01,argv,cached)

      else if (a.lt.-15) then
          ta = -b
          tb = -a
          mult=-1.0
      else if (b.lt.0) then
          ta = -b
          tb = -a
          mult=-1.0
      else
          mult=1.0
      endif


      if (b.gt.15) then !treat b as infinity
          if (ta.le.t4) then
              !normal rejection sampling
              !print *, "nrs",ta,tb
              tnorm = norm_r(ta,tb,mt,mag01,argv,cached)
          else
              !exponential rejection sampling
              tnorm = exp_r(ta,tb,mt,mag01,argv)
              !print *, "ers",ta,tb,tnorm
          endif
      else if (ta.le.0.and.tb.gt.0) then
          if (pnorm(ta).le.t1.or.pnorm(tb).le.t1) then
              !normal rejection sampling
              !print *, "nrs",ta,tb
              tnorm = norm_r(ta,tb,mt,mag01,argv,cached)
          else
              !uniform rejection sampling
              argmax = 0.0
              !print *, "urs",ta,tb
              tnorm = uni_r(ta,tb,mt,mag01,argv, argmax)
          endif
      else !if (a.gt.0) then
          ratio = pnorm(ta) / pnorm(tb)
          if (ratio.lt.t2) then
              !uniform rejection sampling
              argmax = ta
              !print *, "urs",ta,tb
              tnorm = uni_r(ta,tb,mt,mag01,argv, argmax)
          else if (ratio.gt.t1.and.ta.lt.t3) then
              !half-normal rejections sampling
              !print *, "hns", ta,tb
              tnorm = hnorm_r(ta,tb,mt,mag01,argv,cached)

          else
              !exponential rejection sampling
              tnorm = exp_r(ta,tb,mt,mag01,argv)
              !print *, "ers",ta,tb,tnorm
          endif
      endif
      tnorm = tnorm * mult




      
      return
      end function tnorm


      subroutine randv_tnorm(rnd,a, b,mt,mag01,argv,cached,n,na)
      implicit none
      integer n,i,na
      integer mt(624),mag01(2),argv(6)
      real*8 cached(1), rnd(n), tnorm, a(na), b(na)
      
cf2py intent(inout) rnd
cf2py intent(inplace) mt
cf2py intent(in) mag01
cf2py intent(inplace) argv
cf2py intent(inplace) cached

      if (na.eq.1) then
          do i=1,n
              rnd(i) =  tnorm(a(1),b(1), mt,mag01,argv,cached)
          enddo
      else
          do i=1,n
              rnd(i) =  tnorm(a(i),b(i), mt,mag01,argv,cached)
          enddo
      endif

      end subroutine randv_tnorm
      
      
      subroutine randm_tnorm(rnd,a, b, mt,mag01,argv,cached,n,m,na,ma)
      implicit none
      integer n,m,i,j,na,ma
      integer mt(624),mag01(2),argv(6)
      real*8 cached(1), rnd(n,m), tnorm, a(na,ma), b(na,ma)
      
cf2py intent(inout) rnd
cf2py intent(inplace) mt
cf2py intent(in) mag01
cf2py intent(inplace) argv
cf2py intent(inplace) cached

      if (na.eq.1.and.ma.eq.1) then
          do i=1,n
              do j=1,m
                  rnd(i,j) =  tnorm(a(1,1),b(1,1),mt,mag01,argv,cached)
              enddo
          enddo
      else
          do i=1,n
              do j=1,m
                  rnd(i,j) =  tnorm(a(i,j), b(i,j),mt,mag01,argv,cached)
              enddo
          enddo
      endif

      end subroutine randm_tnorm

      subroutine randa3d_tnorm(rnd,a, b, mt,mag01,argv,cached,n,m,r,
     + na,ma,ra)
      implicit none
      integer n,m,r,i,j,k,na,ma,ra
      integer mt(624),mag01(2),argv(6)
      real*8 cached(1), rnd(n,m,r), tnorm, a(na,ma,ra), b(na,ma,ra)
      
cf2py intent(inout) rnd
cf2py intent(inplace) mt
cf2py intent(in) mag01
cf2py intent(inplace) argv
cf2py intent(inplace) cached

      if (na.eq.1.and.ma.eq.1.and.ra.eq.1) then
          do i=1,n
              do j=1,m
                  do k=1,r
                      rnd(i,j,k)= tnorm(a(1,1,1),b(1,1,1),mt,mag01,
     + argv,cached)
                  enddo
              enddo
          enddo
      else
          do i=1,n
              do j=1,m
                  do k=1,r
                      rnd(i,j,k)= tnorm(a(i,j,k),b(i,j,k),mt,mag01,
     + argv,cached)
                  enddo
              enddo
          enddo
      endif
      end subroutine randa3d_tnorm


c     normal rejection sampling
      real*8 function norm_r(a,b,mt,mag01,argv,cached)
      implicit none
      integer mt(624),mag01(2),argv(6)
      real*8 a,b, cached(1),randn
      norm_r=randn(mt,mag01,argv,cached)
      do while (norm_r.lt.a.or.norm_r.gt.b)
          norm_r=randn(mt,mag01,argv,cached)
      enddo
      return
      end function norm_r


c     half normal rejection sampling
      real*8 function hnorm_r(a,b,mt,mag01,argv,cached)
      implicit none
      integer mt(624),mag01(2),argv(6)
      real*8 a,b, cached(1),randn

      hnorm_r=abs(randn(mt,mag01,argv,cached))
      do while(hnorm_r.lt.a.or.hnorm_r.gt.b)
          hnorm_r=abs(randn(mt,mag01,argv,cached))
      enddo
      return
      end function hnorm_r
      
      

c     exponential rejection sampling
      real*8 function exp_r(a,b,mt,mag01,argv)
      implicit none
      integer mt(624),mag01(2),argv(6)
      real*8 a,b
      real*8 lam,randu, genrand_res53,ap, rand_exp

      lam=1.0/a
      randu = genrand_res53(mt,mag01,argv)
      exp_r = a + lam * rand_exp(mt,mag01,argv)
      ap = exp(-0.5*exp_r ** 2) / exp(-a*exp_r)

      do while(randu.gt.ap.or.exp_r.gt.b)
          randu = genrand_res53(mt,mag01,argv)
          exp_r = a + lam * rand_exp(mt,mag01,argv)
          ap = exp(-0.5*exp_r ** 2) / exp(-a*exp_r)
      enddo
      return
      end function exp_r

c     uniform rejection sampling
      real*8 function uni_r(a,b,mt,mag01,argv, argmax)
      implicit none
      integer mt(624),mag01(2),argv(6)
      real*8 a,b,randu, var,argmax,ap, genrand_res53
      real*8 pnorm
      var = b-a

      uni_r = a + genrand_res53(mt,mag01,argv) * var
      randu = genrand_res53(mt,mag01,argv)
      ap = pnorm(uni_r) / pnorm(argmax)
      
      do while(randu.gt.ap)
          uni_r = a + genrand_res53(mt,mag01,argv) * var
          randu = genrand_res53(mt,mag01,argv)
          ap = pnorm(uni_r) / pnorm(argmax)
      enddo
      return
      end function uni_r
      
      
      

      real*8 function pnorm(x)
      implicit none
      real*8 pi,x
      parameter (pi=3.141592653589793)
      pnorm=(2*pi)**(-0.5)*exp(-0.5*x**2)
      
      return
      end function pnorm
      


c-----------------------------------------------------------------------
c     function generates random normal variable
c     code ported from c code in randomkit.c (NumPy library)
c-----------------------------------------------------------------------
      real*8 function randn(mt,mag01,argv,cached)
      implicit none
      integer mt(624),mag01(2),argv(6)
      real*8 cached(1),f,x1,x2,r2, genrand_res53



      if (argv(6).eq.1) then
          !used cached value
          randn = cached(1)
          argv(6) = 0
      else
          r2 = 0.0

          do while(r2.ge.1.0.or.r2.eq.0.0)
              x1 = 2.0 * genrand_res53(mt,mag01,argv) - 1.0
              x2 = 2.0 * genrand_res53(mt,mag01,argv) - 1.0
              r2 = x1 * x1 + x2 * x2
          enddo

          f = sqrt(-2.0 * log(r2)/r2)
          cached = f * x1
          argv(6) = 1
          randn = f * x2
      endif
      return
      end function randn

      subroutine randv_norm(rnd,mt,mag01,argv,cached,n)
      implicit none
      integer n,i
      integer mt(624),mag01(2),argv(6)
      real*8 cached(1), rnd(n), randn
      
cf2py intent(inout) rnd
cf2py intent(inplace) mt
cf2py intent(in) mag01
cf2py intent(inplace) argv
cf2py intent(inplace) cached

      do i=1,n
          rnd(i) =  randn(mt,mag01,argv,cached)
      enddo
      end subroutine randv_norm
      
      
      subroutine randm_norm(rnd,mt,mag01,argv,cached,n,m)
      implicit none
      integer n,m,i,j
      integer mt(624),mag01(2),argv(6)
      real*8 cached(1), rnd(n,m), randn
      
cf2py intent(inout) rnd
cf2py intent(inplace) mt
cf2py intent(in) mag01
cf2py intent(inplace) argv
cf2py intent(inplace) cached

      do i=1,n
          do j=1,m
              rnd(i,j) =  randn(mt,mag01,argv,cached)
          enddo
          
      enddo
      end subroutine randm_norm

      subroutine randa3d_norm(rnd,mt,mag01,argv,cached,n,m,r)
      implicit none
      integer n,m,r,i,j,k
      integer mt(624),mag01(2),argv(6)
      real*8 cached(1), rnd(n,m,r), randn
      
cf2py intent(inout) rnd
cf2py intent(inplace) mt
cf2py intent(in) mag01
cf2py intent(inplace) argv
cf2py intent(inplace) cached

      do i=1,n
          do j=1,m
              do k=1,r
                  rnd(i,j,k) =  randn(mt,mag01,argv,cached)
              enddo
          enddo
          
      enddo
      end subroutine randa3d_norm
c-----------------------------------------------------------------------
c     generates a random number on [0,1) with 53-bit resolution
c-----------------------------------------------------------------------
      real*8 function genrand_res53(mt,mag01,argv)
      integer mt(624),mag01(2),argv(6)
      integer genrand_int32
      double precision a,b
cf2py intent(inplace) mt
cf2py intent(in) mag01
cf2py intent(inplace) argv
      

      a=dble(ishft(genrand_int32(mt,mag01,argv),-5))
      b=dble(ishft(genrand_int32(mt,mag01,argv),-6))
      if(a.lt.0.d0)a=a+2.d0**32
      if(b.lt.0.d0)b=b+2.d0**32
      genrand_res53=(a*67108864.d0+b)/9007199254740992.d0
      return
      end
c-----------------------------------------------------------------------
c     initialize large number (over 32-bit constant number)
c-----------------------------------------------------------------------
      subroutine mt_initln(argv,
     + mag01)
      integer ALLBIT_MASK
      integer TOPBIT_MASK
      integer UPPER_MASK,LOWER_MASK,MATRIX_A,T1_MASK,T2_MASK
      
      integer mag01(0:1), argv(6)

cf2py intent(inout) argv
cf2py intent(inout) mag01

c      common /mt_mask1/ ALLBIT_MASK
c      common /mt_mask2/ TOPBIT_MASK
c      common /mt_mask3/ UPPER_MASK,LOWER_MASK,MATRIX_A,T1_MASK,T2_MASK
c      common /mt_mag01/ mag01
CC    TOPBIT_MASK = Z'80000000'
CC    ALLBIT_MASK = Z'ffffffff'
CC    UPPER_MASK  = Z'80000000'
CC    LOWER_MASK  = Z'7fffffff'
CC    MATRIX_A    = Z'9908b0df'
CC    T1_MASK     = Z'9d2c5680'
CC    T2_MASK     = Z'efc60000'
      TOPBIT_MASK=1073741824
      TOPBIT_MASK=ishft(TOPBIT_MASK,1)
      ALLBIT_MASK=2147483647
      ALLBIT_MASK=ior(ALLBIT_MASK,TOPBIT_MASK)
      UPPER_MASK=TOPBIT_MASK
      LOWER_MASK=2147483647
      MATRIX_A=419999967
      MATRIX_A=ior(MATRIX_A,TOPBIT_MASK)
      T1_MASK=489444992
      T1_MASK=ior(T1_MASK,TOPBIT_MASK)
      T2_MASK=1875247104
      T2_MASK=ior(T2_MASK,TOPBIT_MASK)
      mag01(0)=0
      mag01(1)=MATRIX_A
      argv(2)=UPPER_MASK
      argv(3)=LOWER_MASK
      argv(4)=T1_MASK
      argv(5)=T2_MASK
      return
      end

