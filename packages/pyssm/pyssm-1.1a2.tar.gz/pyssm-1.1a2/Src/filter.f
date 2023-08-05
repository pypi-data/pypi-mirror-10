c Fortran 77 source code for the Python library PySSM
c Copyright (C) 2010  Chris Strickland

c This program is free software: you can redistribute it and/or modify
c it under the terms of the GNU General Public License as published by
c the Free Software Foundation, either version 2 or verion 3 of the
c License.

c This program is distributed in the hope that it will be useful,
c but WITHOUT ANY WARRANTY; without even the implied warranty of
c MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
c GNU General Public License for more details.

c You should have received a copy of the GNU General Public License
c along with this program.  If not, see <http://www.gnu.org/licenses/>.

c ------------------------------------------------------------------
c Filtering and smoothing code + associated functions
c ------------------------------------------------------------------
c Note: Matrix Types [ std = 0, eye = 1, diag = 2, inv = 3, chol = 4 ]
c If type = 3 then matrix is actually the inverse
c If type = 4 then matrix is the cholesky decomposition
c -----------------------------------------------------------------

c     fortran code to simulate disturbance vector for state space model
c     note fl = 1 if rvs on exit is qt & rvs, 0 otherwise
c     note if fl = 1 then gcqt should be gt, otherwise gcqt
      subroutine calc_st_er(gcqt,cqt,rvs,ser,fl,m,r,n,n_q,n_gq)
      implicit none
      integer m,r,n,t,n_q,n_gq,t_q,t_gq,timet,fl
      real*8 gcqt(m,r,n_gq),cqt(r,r,n_q),rvs(r,n),ser(m,n)
      real*8 alpha,beta
c ----------------------
cf2py intent(in) gcqt
cf2py intent(in) cqt
cf2py intent(inplace) rvs
cf2py intent(inplace) ser
cf2py intent(in) fl
cf2py intent(in) m
cf2py intent(in) r
cf2py intent(in) b
c ----------------------
      alpha = 1.0
      beta = 0.0

c$omp parallel default(shared) private(t, t_q, t_gq)
c$omp do schedule(static)
      do t = 1, n
          t_q = timet(n_q, t)
          t_gq = timet(n_gq, t)
          if (fl.eq.1) then
              call dtrmv('l','n','n',r,cqt(:,:,t_q),r,rvs(:,t),1)
          endif
          call dgemv('n',m,r,alpha,gcqt(:,:,t_gq),m,rvs(:,t),1,beta,
     + ser(:,t),1)
      enddo
c$omp end do
c$omp end parallel
      end

c ------------------------------------------------------------------

c     fortran code to simulate disturbance vector for state space model
c     note fl = 1 if rvs on exit is qt & rvs, 0 otherwise
c     note if fl = 1 then gcqt should be gt, otherwise gcqt
      subroutine nt_calc_st_er(gcqt,cqt,rvs,ser,fl,m,r,n)
      implicit none
      integer m,r,n,fl
      real*8 gcqt(m,r),cqt(r,r),rvs(r,n),ser(m,n)
      real*8 alpha,beta
c ----------------------
cf2py intent(in) cqt
cf2py intent(in) gcqt
cf2py intent(inplace) rvs
cf2py intent(inplace) ser
cf2py intent(in) fl
cf2py intent(in) m
cf2py intent(in) r
cf2py intent(in) b
c ----------------------
      alpha = 1.0
      beta = 0.0
      if (fl.eq.1) then
          call dtrmm('l','l','n','n',r,n,alpha,cqt,r,rvs,r)
      endif
      call dgemm('n','n',m,n,r,alpha,gcqt,m,rvs,r,beta,ser,m)
      end

c ------------------------------------------------------------------

c **/** NEW OPENMP ADDED - UNTESTED **/**

c     fortran code for standard filtering and smoothing algorithms
c     simulates data for standard state space model 
      subroutine simssm(y,zt,cht,tt,ser,rvm,av,n,p,m, n_z, n_t, n_h)
      implicit none
      integer n,p,m,t, t_t, t_z, n_z, n_t, t_h, n_h, timet
      real*8 y(p,n), zt(p,m,n_z), cht(p,p,n_h), tt(m,m,n_t)
      real*8 rvm(p,n), ser(m,n), av(m,n) 
      real*8 alpha, beta

c     cht is the sqrt of the ht. recall that ht is a vector
c ----------------------
cf2py intent(inout) y
cf2py intent(in) zt
cf2py intent(in) ch
cf2py intent(in) tt
cf2py intent(in) rvm
cf2py intent(in) ser
cf2py intent(inout) av
cf2py intent(in) n
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n_z
cf2py intent(in) n_t
cf2py intent(in) n_h
c ----------------------
      alpha = 1.0
      beta = 1.0
                  
      do t = 1, n-1      
          t_t = timet(n_t, t)                
          
c         Initialise: av(t+1) = ser(t)          
          call dcopy(m,ser(:,t),1,av(:,t+1),1)

c         Compute: av(t+1) = av(t+1) + tt * av(t)          
          call dgemv('n',m,m,alpha,tt(:,:,t_t),m,av(:,t),1,beta,
     + av(:,t+1),1)
      enddo
      
c$omp parallel default(shared) private(t, t_z, t_h, beta)
c$omp do schedule(static) 
      do t = 1, n
          t_z = timet(n_z, t)          
          t_h = timet(n_h, t)          
          
c         Compute: y(t) = cht(t) * rvm(t)         
          beta = 0.0
          call dgemv('n',p,p,alpha,cht(:,:,t_h),p,rvm(:,t),1,beta,
     + y(:,t),1)
     
c         Compute: y(t) = y(t) + zt(t) * av(t)     
          beta = 1.0
          call dgemv('n',p,m,alpha,zt(:,:,t_z),p,av(:,t),1, beta,
     + y(:,t),1)
      enddo
c$omp end do
c$omp end parallel

      end

c ------------------------------------------------------------------

c     non time varying version that simulates data      
      subroutine ntsimssm(y,zt,ch,tt,ser,rvm,av,n,p,m)
      integer n,p,m,t
      real*8 y(p,n), zt(p,m), ch(p,p), tt(m,m)
      real*8 rvm(p,n),av(m,n),ser(m,n)
      real*8 alpha, beta

c     cht is the sqrt of ht. recall that ht is a vector
c ----------------------
cf2py intent(inout) y
cf2py intent(in) zt
cf2py intent(in) ch
cf2py intent(in) tt
cf2py intent(in) ser
cf2py intent(in) rvm
cf2py intent(inout) av
cf2py intent(in) n
cf2py intent(in) p
cf2py intent(in) m
c ----------------------
      alpha = 1.0
      beta = 1.0
       
      do t = 1, n-1

c         Initialise: av(t+1) = ser(t)      
          call dcopy(m,ser(:,t),1,av(:,t+1),1)          
          
c         Compute: av(t+1) = av(t+1) + tt(t) * av(t)          
          call dgemv('n',m,m,alpha,tt,m,av(:,t),1,beta, av(:,t+1),1)
      enddo

      beta = 0.0
      call dgemm('n','n',p,n,p,alpha,ch,p,rvm,p,beta,y,p)
      beta = 1.0
      call dgemm('n','n',p,n,m,alpha,zt,p,av,m,beta,y,p)
      end

c ------------------------------------------------------------------

c     subroutine for filtering with the standard state SSM
      subroutine filter(y, z, h, tt, qt, nu, k, f, s, a, at, pt, ps,
     + mt, w, ls, lk, wl, ifo, ptt, ilike, pmiss, m, p, n, n_z, n_t,
     +  n_q, n_h)
      integer m, p, n, t, i, ifo, ptt, info, ilike
      integer timet, n_z, n_t, n_q, t_z, t_t, t_q, t_h, pmiss(n)
      real*8 y(p,n), z(p,m,n_z), h(p,p,n_h), tt(m,m,n_t), qt(m,m,n_q)
      real*8 nu(p,n), k(m,p,n), s(p,m,n), ls(m,m,n), a(m,n)
      real*8 ps(m,m,n), mt(m,p), at(m), pt(m,m), f(p,p), w(m,m)
      real*8 alpha, beta, lk(*), wl(p), logdet, ddot, llike
c ----------------------
cf2py intent(in) y
cf2py intent(in) z
cf2py intent(in) h
cf2py intent(in) tt
cf2py intent(in) qt
cf2py intent(inout) nu
cf2py intent(inout) k
cf2py intent(in) f
cf2py intent(inout) s
cf2py intent(inout) a
cf2py intent(in) at
cf2py intent(in) pt
cf2py intent(inout) ps
cf2py intent(in) mt
cf2py intent(in) w
cf2py intent(inplace) lk
cf2py intent(inplace) ifo
cf2py intent(in) pmiss
cf2py intent(in) ptt
cf2py intent(in) m
cf2py intent(in) p
cf2py intent(in) n
cf2py intent(in) n_z
cf2py intent(in) n_t
cf2py intent(in) n_h
cf2py intent(in) n_q
c ----------------------
c     note if lk(1).lt.-1 then calculate likelihood and return in lk(1)

      ifo = 0
      llike = 0.0

      do t = 1, n
          t_z = timet(n_z, t)
          t_t = timet(n_t, t)
          t_q = timet(n_q, t)
          t_h = timet(n_h, t)
      
c         1. Initialise: a(:,t) = at      
          call dcopy(m,at,1,a(:,t),1)
c         -------------------------------------------------------------
c         2. Initialise: ps(:,i,t) = pt(:,i)          
          do i = 1, m
              call dcopy(m, pt(:,i), 1, ps(:,i,t), 1)
          enddo
c         -------------------------------------------------------------
c         3. Compute: Nu(t) = Y(t) - Z(t) * a(t)     
c         3a. Initialise: nu(:,t) = y(:,t)
          if (pmiss(t).eq.0) then
              !data not missing
              call dcopy(p, y(:,t), 1, nu(:,t), 1)
c             3b. Compute: nu = nu - z * at          
              alpha = -1.0
              beta = 1.0          
              call dgemv('n',p,m,alpha,z(:,:,t_z),p,at,1,beta,nu(:,t),1)
c         -------------------------------------------------------------                    
c             4. Compute: m(t) = P(t)*Z(t)'   [i.e. (m,p) = (m,m) *(m,p) ]
              alpha = 1.0
              beta = 0.0         
              call dgemm('n','t',m,p,m,alpha,pt,m,z(:,:,t_z),p,beta,mt,
     + m)
c         -------------------------------------------------------------
c             5. Compute: F(t) = Z(t)*m(t) + H(t)  [i.e. (p,p) = (p,m)*(m,p) ]        
c             5a. Initialise: f(:,i) = h(:,i,t_h)
              !column of y not missing
              do i = 1, p
                  call dcopy(p, h(:,i,t_h), 1, f(:,i), 1)
              enddo
c             5b. Compute: f = f + z * mt          
              beta = 1.0
              call dgemm('n','n',p,p,m,alpha,z(:,:,t_z),p,mt,m,beta,f,p)
!             print *, "ft =", f          
c         -------------------------------------------------------------
c             6. Compute: S(t) = inv(F(t))*Z(t)     [i.e. solve F.S = Z ]
c             6a. Initialise: s = z
              do i = 1, m
                  call dcopy(p, z(:,i,t_z), 1, s(:,i,t), 1)
              enddo
c             6b. Solve: f * x = s   [Note: store x in s]  [i.e. (p,p) *(p,m) = (p,m)  ]
              call dposv('u',p,m,f,p,s(:,:,t),p,info)
              if (info.ne.0) then
                  ifo = 1
              endif                          
          !else
              !column of y missing so set S(t)=0
          !    do i=1,m
          !        do j=1,m
          !            S(i,j,t)=0.0
          !        enddo
          !    enddo
c         ------------------------------------------------------------          
              if (ilike.eq.0) then

c                 Compute: logdet = 2.0 * sum(i: log(f(i,i))          
                  logdet = 0.0
                  do i = 1, p
                      logdet = logdet + log(f(i,i))
                  enddo
                  logdet = 2.0 * logdet
                  
c                 Initialise: wl = nu(:,t)              
                  call dcopy(p, nu(:,t), 1, wl, 1)

c                 Solve:  f.x = wl  (i.e. Compute: x = inv[f]*wl ) (Note: store x as wl)
                  call dtrsv('u','t','n',p,f,p,wl,1)
                  
c                 Subtract: -(0.5 * nu^2) - (0.5 * logdet)                           
                  llike = llike - 0.5 * (logdet + ddot(p,wl,1,wl,1))

              endif
c             -------------------------------------------------------------          
c             7. Compute: W(t) = T(t)*P(t)
              beta = 0.0
              if (ptt.eq.0) then
c                 7a. Compute: w = tt * pt
                  call dgemm('n','n', m, m, m, alpha, tt(:,:,t_t),
     + m, pt, m, beta, w, m)
              else
c                 7b. Initialise: w = pt          
                  do i = 1, m
                      call dcopy(m,pt(:,i),1,w(:,i),1)
                  enddo
              endif
c             -------------------------------------------------------------          
c             8. Compute: K(t) = W(t) * S(t)'
              call dgemm('n','t',m,p,m,alpha,w,m,s(:,:,t),p,beta,
     + k(:,:,t),m)
!              print *, "kt =", k(:,:,t)
c             -------------------------------------------------------------
c             9. Compute: L(t) = T(t) - K(t)*Z(t)   [i.e.  (m,m) = (m,p) * (p,m) ] 
c             9a. Initialise: ls(:,i,t) = tt(:,t,t_t)
              do i = 1, m
                  call dcopy(m,tt(:,i,t_t),1,ls(:,i,t),1)
              enddo
c             9b. Compute: ls = ls - k(:,:,t) *  z(:,:,t_z)   [i.e. (m,m) = (m,p) * (p,m) ]
              alpha = -1.0
              beta = 1.0
              call dgemm('n','n',m,m,p,alpha,k(:,:,t),m,z(:,:,t_z),p,
     + beta,
     + ls(:,:,t),m)        
!              print *, "lt =", ls(:,:,t)
c             -------------------------------------------------------------          
c             10. Compute: a(t+1) = T(t)*a(t) + K(t)*nu(t)
              alpha = 1.0
              beta = 0.0
              if (ptt.eq.0) then
c                 10a. Compute: at = tt(:,:,t_t) * a(:,t)          
                  call dgemv('n',m,m,alpha,tt(:,:,t_t),m,a(:,t),1,beta,
     + at,1)
              else
c                 10a. Initialise: at = a(:,t)          
                  call dcopy(m, a(:,t), 1, at, 1)
              endif
c             10b. Compute: at = at + k(:,:,t) * nu(:,t)   [i.e. (m) = (m,p) *(p)   ]
              beta = 1.0
              call dgemv('n',m,p,alpha,k(:,:,t),m,nu(:,t),1,beta,at,1)
              beta = 0.0
!              print *, "at =", at
          else
              !Compute L(t)=T(t)
              do i = 1, m
                  call dcopy(m,tt(:,i,t_t),1,ls(:,i,t),1)
              enddo
c             10b. Compute a(t+1) = T(t)*a(t)
              alpha = 1.0
              beta = 0.0
              if (ptt.eq.0) then
c                 10a. Compute: at = tt(:,:,t_t) * a(:,t)          
                  call dgemv('n',m,m,alpha,tt(:,:,t_t),m,a(:,t),1,beta,
     + at,1)
              else
c                 10a. Initialise: at = a(:,t)          
                  call dcopy(m, a(:,t), 1, at, 1)
              endif
c             10b. Compute: W(t) = T(t)*P(t)
              beta = 0.0
              if (ptt.eq.0) then
c                 Compute: w = tt * pt
                  call dgemm('n','n', m, m, m, alpha, tt(:,:,t_t),
     + m, pt, m, beta, w, m)
              else
c                 Initialise: w = pt          
                  do i = 1, m
                      call dcopy(m,pt(:,i),1,w(:,i),1)
                  enddo
              endif
          endif

c         -------------------------------------------------------------          
c         11. Compute: P(t+1) = W(t)*L(t)' + Q(t)
c         call dgemm('n','n',m,m,m,alpha,tt(:,:,t),m,pt,m,beta,w,m)
c         11a. Initialise: pt = qt(:,:,t_q) 
          do i = 1, m
              call dcopy(m, qt(:,i,t_q), 1, pt(:,i), 1)
          enddo
c         11b. Compute: pt = pt + w * ls' where w = tt * pt  
c         [i.e. (m,m) = (m,m) * (m,m) * (m,m) ]
          beta = 1.0
          call dgemm('n','t',m,m,m,alpha,w,m,ls(:,:,t),m,beta,pt,m)
      enddo
c     -------------------------------------------------------------
      lk(1)=llike
      end

c ------------------------------------------------------------------

c     subroutine for filtering with the standard non time varying state SSM
      subroutine ntfilter(y,z,h,tt,qt,nu,k,f,s,a,at,pt,ps,mt,w,ls,lt,
     + lk,wl,ifo,ilike,m,p,n)
      integer m,p,n,t,i,ifo,info,chk,indr,lt,ilike
      real*8 y(p,n),z(p,m),h(p,p),tt(m,m),qt(m,m),lk,wl(p)
      real*8 nu(p,n),k(m,p,n),s(p,m,n),ls(m,m,n),a(m,n)
      real*8 ps(m,m,n),mt(m,p),at(m),pt(m,m),f(p,p),w(m,m)
      real*8 alpha, beta,fnorm, tol,logdet,llike,ddot, temp
c ----------------------
cf2py intent(in) y
cf2py intent(in) z
cf2py intent(in) h
cf2py intent(in) tt
cf2py intent(in) qt
cf2py intent(inplace) nu
cf2py intent(inplace) k
cf2py intent(in) f
cf2py intent(inplace) s
cf2py intent(inplace) a
cf2py intent(in) at
cf2py intent(in) pt
cf2py intent(inplace) ps
cf2py intent(in) mt
cf2py intent(in) w
cf2py intent(inout) lk
cf2py intent(in) wl
cf2py intent(inout) ifo
cf2py intent(inout) lt
cf2py intent(in) m
cf2py intent(in) p
cf2py intent(in) n
c ----------------------
      ifo = 0
      tol = 1E-10
      chk = 10
      indr = 0  ! Indicator for steady state
      lt = n+1
      llike = 0.0
       
      do t = 1, n
c         Not yet reached steady state:      
          if (indr.eq.0) then
          
c             1. Initialise: a(:,t) = at           
              call dcopy(m,at,1,a(:,t),1)
c             ------------------------------
c             2. Initialise: ps(:,:,t)  = pt
              do i = 1, m
                  call dcopy(m,pt(:,i),1,ps(:,i,t),1)
              enddo
c             ------------------------------              
c             3. Compute: Nu(t) = Y(t) - Z(t)*a(t)     
c             3a. Initialise nu(:,t) = y(:, t)
              call dcopy(p, y(:,t), 1, nu(:,t), 1)
              
c             3b. Compute: nu(:,t) = nu(:,t) - z * at      
              alpha = -1.0
              beta = 1.0                                 
              call dgemv('n',p,m,alpha,z,p,at,1,beta,nu(:,t),1)
                            
c             ------------------------------
c             4. Compute: m(t) = P(t)*Z(t)' , i.e. mt = pt * z
              alpha = 1.0
              beta = 0.0
              call dgemm('n','t',m,p,m,alpha,pt,m,z,p,beta,mt,m)
c             ------------------------------
c             5. Compute: F(t) = Z(t)*m(t) + H(t)    
c             5a. Initialise f(:,i) = h(:,i)      
              do i = 1, p
                  call dcopy(p,h(:,i),1,f(:,i),1)
              enddo                            
c             5b. Compute: f = f + z*mt
              beta = 1.0
              call dgemm('n','n',p,p,m,alpha,z,p,mt,m,beta,f,p)
c             ------------------------------              
c             6. Compute: F(t)*S(t) = Z(t); solve for S(t)=inv(F(t))*Z(t)          
c             6a.Initialise s(:,:,t) = z
              do i = 1, m
                  call dcopy(p,z(:,i),1,s(:,i,t),1)
              enddo
c             6b. Solve f . x =  s and set s = x             
              call dposv('u',p,m,f,p,s(:,:,t),p,info)
              if (info.ne.0) then
                  ifo = 1
              endif
              
!              if(t.eq.1) then
!                  print *, "S = ", s(:,:,t)
!              endif
c             ------------------------------              
              beta = 0.0
              
              if (ilike.eq.0) then
                  logdet = 0.0
                  do i = 1, p
                      logdet = logdet + log(f(i,i))
                  enddo
                  logdet = 2.0 * logdet

c                 Initialise wl = nu(:,t)                  
                  call dcopy(p,nu(:,t),1,wl,1)
                  
                  call dtrsv('u','t','n',p,f,p,wl,1)
                  
                  llike = llike-0.5*(logdet+ddot(p,wl,1,wl,1))
                  
c                  call dcopy(p,nu(:,t),1,wl,1)
c                  call dtrsm('l','u','t','n',p,1,alpha,f,p,wl,p)
c                  call dtrsm('l','u','n','n',p,1,alpha,f,p,wl,p)
c                  llike = llike-0.5*(logdet+ddot(p,wl,1,nu(:,t),1))
              endif
c             ------------------------------          
c             7. Compute: W(t) = T(t)*P(t),   i.e. w = tt * pt
              call dgemm('n','n',m,m,m,alpha,tt,m,pt,m,beta,w,m)
c             ------------------------------              
c             8. Compute: K(t) = W(t)*S(t)',  i.e. k = w * s
              call dgemm('n','t',m,p,m,alpha,w,m,s(:,:,t),p,beta,
     + k(:,:,t),m)
!              if(t.eq.1) then
!                  print *, "K = ", k(:,:,t)
!              endif
c             ------------------------------     
c             9.  Compute: L(t)= T(t) - K(t)*Z(t)
c             9a. Initialise ls(:,:,t) = tt 
              do i = 1, m
                  call dcopy(m,tt(:,i),1,ls(:,i,t),1)
              enddo             
c             9b. Compute: ls = ls - k * z 
              alpha = -1.0
              beta = 1.0             
              call dgemm('n','n',m,m,p,alpha,k(:,:,t),m,z,p,beta,
     + ls(:,:,t),m)
!              if(t.eq.1) then
!                  print *, "L = ", ls(:,:,t)
!              endif
c             ------------------------------
c             Monitor convergence to steady state
              if(t.gt.chk) then
                  if(mod(t,chk).eq.0) then 
                      temp = fnorm(ps(:,:,t),ps(:,:,t-chk),m,m)
                      if(temp.lt.tol) then
                          indr = 1
                          lt = t
                      endif                
                  endif
              endif
c             ------------------------------
c             10. Compute: a(t+1)= T(t)*a(t) + K(t)*nu(t)
c             10a. Compute: at = tt * a
              alpha = 1.0
              beta = 0.0
              call dgemv('n',m,m,alpha,tt,m,a(:,t),1,beta,at,1)
c             10b. Compute: at = at + k * nu              
              beta = 1.0
              call dgemv('n',m,p,alpha,k(:,:,t),m,nu(:,t),1,beta,at,1)
c             ------------------------------
c             11. Compute: P(t+1)= W(t)*L(t)' + Q(t)
c             11a. Initialise: pt = qt
              do i = 1, m
                  call dcopy(m,qt(:,i),1,pt(:,i),1)
              enddo              
c             11b. Compute: pt = pt + w*ls 
              beta = 1.0             
              call dgemm('n','t',m,m,m,alpha,w,m,ls(:,:,t),m,beta,pt,m)

c         Reached steady state:          
          else              
              call dcopy(m,at,1,a(:,t),1)
c              do i=1,m
c                  call dcopy(m,pt(:,i),1,ps(:,i,t),1)
c              enddo
c             ------------------------------
c             12. Compute: Nu(t)= Y(t) - Z(t)*a(t)    
c             12a. Initialise: nu = y 
              call dcopy(p,y(:,t),1,nu(:,t),1)              
c             12b. Compute: nu = nu + z * at 
              alpha = -1.0
              beta = 1.0             
              call dgemv('n',p,m,alpha,z,p,at,1,beta,nu(:,t),1)
              
!               if(t.eq.1) then
!                  print *, "nu = ", nu(:,t)
!              endif
c             ----------------------------------------            
              if (ilike.eq.0) then
                  call dcopy(p,nu(:,t),1,wl,1)
                  call dtrsv('u','t','n',p,f,p,wl,1)
                  llike = llike - 0.5*(logdet+ddot(p,wl,1,wl,1))
c              call dtrsm('l','u','t','n',p,1,alpha,f,p,wl,p)
c              call dtrsm('l','u','n','n',p,1,alpha,f,p,wl,p)
c              llike=llike-0.5*(logdet+ddot(p,wl,1,nu(:,t),1))
              endif      
c             ------------------------------
c             13. Compute: a(t+1)= T(t)*a(t)+K(t)*nu(t)
c             13a. Compute: at = tt * a
              alpha = 1.0
              beta = 0.0
              call dgemv('n',m,m,alpha,tt,m,a(:,t),1,beta,at,1)
c             ------------------------------                            
c             14. Compute: at = at + k * nu              
c             Note: lt replaces t in k, i.e. k(:,:,lt)              
              beta = 1.0
              call dgemv('n',m,p,alpha,k(:,:,lt),m,nu(:,t),1,beta,at,1)
              beta = 0.0
c             ------------------------------              
c             P(t+1) = W(t)*L(t)' + Q(t)
              do i=1,m
                  call dcopy(m,qt(:,i),1,pt(:,i),1)
              enddo
              beta = 1.0
              call dgemm('n','t',m,m,m,alpha,w,m,ls(:,:,lt),m,beta,pt,m)

          endif
      enddo
      
      lk = llike
      end

c ------------------------------------------------------------------
c     benchmark subroutine for filtering with the standard state SSM
      subroutine bfilter(y,z,h,tt,qt,nu,k,f,fi,wz,a,at,pt,ps,mt,w,ls,
     + ifo, m, p, n, n_h, n_t, n_q, n_z)
      integer m,p,n,t,i,ifo, info
      integer n_h, n_t, n_q, n_z, t_t, t_z, t_h, t_q, timet
      real*8 y(p,n),z(p,m,n_z),h(p,p,n_h),tt(m,m,n_t),qt(m,m,n_q)
      real*8 nu(p,n),k(m,p,n),fi(p,p,n),ls(m,m,n),a(m,n),wz(m,p)
      real*8 ps(m,m,n),mt(m,p),at(m),pt(m,m),f(p,p),w(m,m)
      real*8 alpha, beta
c ----------------------
cf2py intent(in) y
cf2py intent(in) z
cf2py intent(in) h
cf2py intent(in) tt
cf2py intent(in) qt
cf2py intent(inout) nu
cf2py intent(inout) k
cf2py intent(in) f
cf2py intent(inout) fi
cf2py intent(in) wz
cf2py intent(inout) s
cf2py intent(inout) a
cf2py intent(in) at
cf2py intent(in) pt
cf2py intent(inout) ps
cf2py intent(in) mt
cf2py intent(in) w
cf2py intent(inout) ifo
cf2py intent(in) m
cf2py intent(in) p
cf2py intent(in) n
cf2py intent(in) n_z
cf2py intent(in) n_t
cf2py intent(in) n_h
cf2py intent(in) n_q
c ----------------------
      ifo = 0

      do t = 1, n
      
          t_q = timet(n_q, t)
          t_z = timet(n_z, t)
          t_h = timet(n_h, t)
          t_t = timet(n_t, t)
      
          call dcopy(m,at,1,a(:,t),1)
          do i = 1, m
              call dcopy(m,pt(:,i),1,ps(:,i,t),1)
          enddo
          
c         Nu(t)= Y(t) - Z(t)*a(t)     
          call dcopy(p,y(:,t),1,nu(:,t),1)
          alpha=-1.0
          beta=1.0
          call dgemv('n',p,m,alpha,z(:,:,t_z),p,at,1,beta,nu(:,t),1)
          alpha=1.0
          beta=0.0
          
c         m(t) = P(t)*Z(t)'          
          call dgemm('n','t',m,p,m,alpha,pt,m,z(:,:,t_z),p,beta,mt,m)

c         F(t) = Z(t)*m(t)+H(t)          
          do i=1,p
              call dcopy(p,h(:,i,t_h),1,f(:,i),1)
          enddo
          beta=1.0
          call dgemm('n','n',p,p,m,alpha,z(:,:,t_z),p,mt,m,beta,f,p)

c         calculate fi = inverse(f)          
          call eye(fi(:,:,t),p)
          call dposv('u',p,p,f,p,fi(:,:,t),p,info)
          if (info.ne.0) then
              ifo=1
          endif
          beta=0.0
          
c         W(t) = T(t)*P(t)
          call dgemm('n','n',m,m,m,alpha,tt(:,:,t_t),m,pt,m,beta,w,m)

c         K(t) = W(t)*Z(t)'*inv(F(t))
          call dgemm('n','t',m,p,m,alpha,w,m,z(:,:,t_z),p,beta,wz,m)
          call dgemm('n','n',m,p,p,alpha,wz,m,fi(:,:,t),p,beta,
     + k(:,:,t),m)

c         L(t)=T(t)-K(t)*Z(t)
          do i=1,m
              call dcopy(m,tt(:,i,t_t),1,ls(:,i,t),1)
          enddo
          alpha=-1.0
          beta=1.0
          call dgemm('n','n',m,m,p,alpha,k(:,:,t),m,z(:,:,t_z),p,beta,
     + ls(:,:,t),m)

          alpha=1.0
          beta=0.0
          
c         a(t+1)=T(t)*a(t)+K(t)*nu(t)
          call dgemv('n',m,m,alpha,tt(:,:,t_t),m,a(:,t),1,beta,at,1)
          beta=1.0
          call dgemv('n',m,p,alpha,k(:,:,t),m,nu(:,t),1,beta,at,1)
          beta=0.0
          
c         P(t+1)=W(t)*L(t)'+Q(t)
c          call dgemm('n','n',m,m,m,alpha,tt(:,:,t),m,pt,m,beta,w,m)
          do i=1,m
              call dcopy(m,qt(:,i,t_q),1,pt(:,i),1)
          enddo
          beta=1.0
          call dgemm('n','t',m,m,m,alpha,w,m,ls(:,:,t),m,beta,pt,m)
      enddo
      end

c ------------------------------------------------------------------

c     contemporaneous version of the kalman filter
c     subroutine for filtering with the standard state SSM
      subroutine cfilter(y,z,h,tt,qt,nu,f,s,a,at,pt,ps,mt,w,lk,wl,ifo,
     + ilike, m, p, n, n_z, n_t, n_h, n_q)
      integer m,p,n,t,i,ifo, info,ilike
      integer n_z, n_t, n_h, n_q, t_z, t_t, t_h, t_q, timet
      real*8 y(p,n),z(p,m,n_z),h(p,p,n_h),tt(m,m,n_t),qt(m,m,n_q)
      real*8 nu(p,n),s(p,m,n),a(m,n+1)
      real*8 ps(m,m,n+1),mt(p,m),at(m,n),pt(m,m,n),f(p,p),w(m,m,n)
      real*8 alpha, beta,lk(*),logdet,ddot,llike,wl(p)
c ----------------------
cf2py intent(in) y
cf2py intent(in) z
cf2py intent(in) h
cf2py intent(in) tt
cf2py intent(in) qt
cf2py intent(inout) nu
cf2py intent(inout) k
cf2py intent(in) f
cf2py intent(inout) s
cf2py intent(inout) a
cf2py intent(in) at
cf2py intent(in) pt
cf2py intent(inout) ps
cf2py intent(in) mt
cf2py intent(in) w
cf2py intent(inout) lk
cf2py intent(in) wl
cf2py intent(inout) ifo
cf2py intent(in) m
cf2py intent(in) p
cf2py intent(in) n
cf2py intent(in) n_t
cf2py intent(in) n_q
cf2py intent(in) n_z
cf2py intent(in) n_h
c ----------------------
c     note if lk(1).lt.-1 then calculate likelihood and return in lk(1)

      ifo=0
      llike=0.0

      do t=1,n
      
          t_t = timet(n_t, t)
          t_z = timet(n_z, t)
          t_q = timet(n_q, t)
          t_h = timet(n_h, t)
      
c         Nu(t)= Y(t) - Z(t)*a(t)     
          call dcopy(p,y(:,t),1,nu(:,t),1)
          alpha=-1.0
          beta=1.0
          call dgemv('n',p,m,alpha,z(:,:,t_z),p,a(:,t),1,beta,nu(:,t),1)
          alpha=1.0
          beta=0.0
          
c         m(t) = Z(t)*P(t)          
          call dgemm('n','n',p,m,m,alpha,z(:,:,t_z),p,ps(:,:,t),m,beta,
     + mt,p)
     
c         F(t) = m(t)*Z(t)'+H(t)          
          do i=1,p
              call dcopy(p,h(:,i,t_h),1,f(:,i),1)
          enddo
          beta=1.0
          call dgemm('n','t',p,p,m,alpha,mt,p,z(:,:,t_h),p,beta,f,p)
          
c         F(t)*S(t) = m(t); solve for S(t)=inv(F(t))*m(t)          
          do i=1,m
              call dcopy(p,mt(:,i),1,s(:,i,t),1)
          enddo
          call dposv('u',p,m,f,p,s(:,:,t),p,info)
          if (info.ne.0) then
              ifo=1
          endif
          beta=0.0

          if (ilike.eq.0) then
              logdet=0.0
              do i=1,p
                  logdet=logdet+log(f(i,i))
              enddo
              logdet=2.0*logdet
              call dcopy(p,nu(:,t),1,wl,1)
              call dtrsv('u','t','n',p,f,p,wl,1)
              llike=llike-0.5*(logdet+ddot(p,wl,1,wl,1))
c              call dtrsm('l','u','t','n',p,1,alpha,f,p,wl,p)
c              call dtrsm('l','u','n','n',p,1,alpha,f,p,wl,p)
c              llike=llike-0.5*(logdet+ddot(p,wl,1,nu(:,t),1))
          endif
          
c         a(t|t)=a(t)+S(t)'nu(t)
          alpha=1.0
          beta=1.0
          call dcopy(m,a(:,t),1,at(:,t),1)
          call dgemv('t',p,m,alpha,s(:,:,t),p,nu(:,t),1,beta,at(:,t),1)

c         P(t|t)=P(t)-m(t)'S(t)
          do i=1,m
              call dcopy(m,ps(:,i,t),1,pt(:,i,t),1)
          enddo
          alpha=-1.0
          beta=1.0
          call dgemm('t','n',m,m,p,alpha,mt,p,s(:,:,t),p,beta,
     + pt(:,:,t),m)

c         W(t) = P(t)*T(t)'
          alpha=1.0
          beta=0.0
          call dgemm('n','t',m,m,m,alpha,pt(:,:,t),m,tt(:,:,t_t),m,beta,
     + w(:,:,t), m)

c         a(t+1)=T(t)*a(t|t)
          call dgemv('n',m,m,alpha,tt(:,:,t_t),m,at(:,t),1,beta,
     + a(:,t+1), 1)

c         P(t+1)=T(t)*W(t)+Q(t)
          beta=1.0
          do i=1,m
              call dcopy(m,qt(:,i,t),1,ps(:,i,t+1),1)
          enddo
          call dgemm('n','n',m,m,m,alpha,tt(:,:,t),m,w(:,:,t),m,beta,
     + ps(:,:,t+1),m)

      enddo
      lk(1)=llike
      end

c ------------------------------------------------------------------
c     contemporaneous version of the kalman filter
c     subroutine for filtering with the standard state SSM
c     non-time varying system matricies

      subroutine ntcfilter(t_last,y,z,h,tt,qt,nu,f,s,a,at,pt,ps,mt,
     + w, lk, wl,ifo, ilike, m,p,n)
     
      integer m,p,n,t,it,t_last,i,ifo,info,ilike,chk,flag_steady
      real*8 y(p,n),z(p,m),h(p,p),tt(m,m),qt(m,m), tol
      real*8 nu(p,n),s(p,m,n),a(m,n+1),fnorm
      real*8 ps(m,m,n+1),mt(p,m),at(m,n),pt(m,m,n),f(p,p),w(m,m,n)
      real*8 alpha, beta,lk(*),logdet,ddot,llike,wl(p), temp
c ----------------------
cf2py intent(inout) t_last
cf2py intent(in) y
cf2py intent(in) z
cf2py intent(in) h
cf2py intent(in) tt
cf2py intent(in) qt
cf2py intent(inout) nu
cf2py intent(inout) k
cf2py intent(in) f
cf2py intent(inout) s
cf2py intent(inout) a
cf2py intent(inout) at
cf2py intent(in) pt
cf2py intent(inout) ps
cf2py intent(in) mt
cf2py intent(in) w
cf2py intent(inout) lk
cf2py intent(in) wl
cf2py intent(inout) ifo
cf2py intent(in) m
cf2py intent(in) p
cf2py intent(in) n
c ----------------------
c     Note: ps == P(t)
c     note if lk(1).lt.-1 then calculate likelihood and return in lk(1)    
  
      chk = 10
      ifo = 0
      t_last = n + 1      
      tol = 1E-10
      logdet = 0.0
      llike = 0.0
      flag_steady = 0  ! Indicator that steady state reached
      
      do t = 1, n
      
c         1. Compute: Nu(t)= Y(t) - Z(t)*a(t)     
c         1a. Initialise: nu(:,t) = y(:,t)
          call dcopy(p,y(:,t),1,nu(:,t),1)          
c         1b. Compute: nu(:,t) = nu(:,t) + z * a(:,t)          
          alpha = -1.0
          beta = 1.0
          call dgemv('n',p,m,alpha,z,p,a(:,t),1,beta,nu(:,t),1)
c         ---------------------------------------
c         NOTE: Step 2 - 7 do not need to be computed once steady state reached
          if(flag_steady.eq.0) then
          
c             2. Compute: m(t) = Z(t)*P(t), i.e.  mt = z * ps(:,:,t)        
              alpha = 1.0
              beta = 0.0
              call dgemm('n','n',p,m,m,alpha,z,p,ps(:,:,t),m,beta,
     + mt,p)
c             ---------------------------------------           
c             3. Compute: F(t) = m(t)*Z(t)'+ H(t)          
c             3a. Initialise: f(:,:) = h(:,:)
              do i = 1, p
                  call dcopy(p, h(:,i), 1, f(:,i), 1)
              enddo          
c             3b. Compute: f = f + mt * z'
              beta = 1.0
              call dgemm('n','t',p,p,m,alpha,mt,p,z,p,beta,f,p)
c             ---------------------------------------                     
c             Calculate log-likelihood component
              if (ilike.eq.0) then  
                  logdet = 0.0
                  do i = 1, p
                      logdet = logdet + 2.0 * log(f(i,i))
                  enddo                
              endif          
c             ---------------------------------------                     
c             4. Compute: S(t) = inv(F(t)) * m(t)  
c             by solving system  F(t)*S(t) = m(t)
c             4a. Initialise s(:,:,t) = mt
              do i = 1, m
                  call dcopy(p,mt(:,i),1,s(:,i,t),1)
              enddo
c             4b. Solve f x = s  and set s = x       
              call dposv('u',p,m,f,p,s(:,:,t),p,info)
              if (info.ne.0) then
                  ifo = 1
                  print *, 'Error: Failed to solve [ntcfilter:4b]'
              endif
c             ---------------------------------------                                
c             5. Compute: P(t|t) = P(t) - S(t)'m(t)
c             5a. Initialise: pt(:,:,t) = ps(:,:,t)
              do i = 1, m
                  call dcopy(m,ps(:,i,t),1,pt(:,i,t),1)
              enddo
c             5b. Compute: pt = pt - s' * mt
              alpha = -1.0
              beta = 1.0
              call dgemm('t','n',m,m,p,alpha,s(:,:,t),p,mt,p,beta,
     + pt(:,:,t),m)   
c             ---------------------------------------                     
c             6. Compute: W(t) = T(t) * P(t|t), i.e. w = tt * pt
              alpha = 1.0
              beta = 0.0
              call dgemm('n','t',m,m,m,alpha,tt,m,pt(:,:,t),m,beta,
     + w(:,:,t), m)
c             ---------------------------------------                     
c             7. Compute: P(t+1) = W(t)*T(t)' + Q(t)
c             7a. Initialise: ps(:,:, t+1) = qt
              beta = 1.0
              do i = 1, m
                  call dcopy(m,qt(:,i),1,ps(:,i,t+1),1)
              enddo
c             7b. Compute: ps = ps + w * tt'
              call dgemm('n','t',m,m,m,alpha,w(:,:,t),m,tt,m,beta,
     + ps(:,:,t+1),m)
c             ---------------------------------------           
          endif ! FINISH CALCS FOR NO STEADY STATE SITUATION
c         ----------------------------------------------------          
c         NOTE: This must always be computed at time t          
          if (ilike.eq.0) then              
c            Initialise: wl = nu(:,t)
             call dcopy(p,nu(:,t),1,wl,1)             
c            Solve: f x = wl  and set wl = x            
             call dtrsv('u','t','n',p,f,p,wl,1)
             
             llike = llike -0.5*(logdet + ddot(p,wl,1,wl,1))
          endif       
          
          if (flag_steady.eq.0) then 
              it = t
          else
              it = t_last
          endif     
c         ---------------------------------------                     
c         NOTE: Step 8 and 9 must always be computed at time t           
c         8. Compute: a(t|t) = a(t) + S(t)'nu(t)
          alpha = 1.0
          beta = 1.0
c         8a. Initialise: at(:,t) = a(:,t)          
          call dcopy(m,a(:,t),1,at(:,t),1)
c         8b. Compute: at = at  + s' * nu     
c         NOTE: s(:,:,t or lt)  depending on whether steady state reached  
          call dgemv('t',p,m,alpha,s(:,:,it),p,nu(:,t),1,beta,at(:,t),1)
c         ---------------------------------------           
c         9. Compute: a(t+1) = T(t) * a(t|t), i.e. a = tt * at
          call dgemv('n',m,m,alpha,tt,m,at(:,t),1,beta,a(:,t+1),
     + 1)
c         ---------------------------------------                
c         Monitor convergence to steady state if not already occurred
          if (flag_steady.eq.0) then   ! i.e  Not yet reached 
              if(t.gt.chk) then  
                  if (mod(t,chk).eq.0) then   ! i.e. check regularly
                      temp = fnorm(ps(:,:,t),ps(:,:,t-chk),m,m)
                      if(temp.lt.tol) then
                          flag_steady = 1    ! Update flag                  
                          t_last = t   ! Record when steady state occurs
                      endif
                  endif
              endif
          endif
                    
      enddo  
      
      lk(1) = llike
      
      end

c ------------------------------------------------------------------

c     subroutine for smoothing. Standard state space model. Time varying
c     system matricies.
      subroutine smoother(ah,s,nu,ls,r,ltr,as,ps,pmiss,p,m,n) 
      integer p,m,n,t,i,pmiss(n)
      real*8 ah(m,n),s(p,m,n),nu(p,n),ls(m,m,n),r(m),ltr(m)
      real*8 as(m,n), ps(m,m,n)
      real*8 alpha, beta
c ----------------------
cf2py intent(inout) ah
cf2py intent(in) s
cf2py intent(in) nu
cf2py intent(in) ls
cf2py intent(in) r
cf2py intent(in) ltr
cf2py intent(in) as
cf2py intent(in) ps
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n
c ----------------------
c     Initialise vector
      do i = 1, m
          r(i) = 0.0
      enddo

      alpha = 1.0
      
      do t = n, 1, -1
      
c         Step 1: Compute r(t-1) = S(t)' * nu(t)  +  L(t)' * r(t)          
          beta = 0.0
          
c         1a. Compute: ltr = ls(:,:,t) * r          
          call dgemv('t',m,m,alpha,ls(:,:,t),m,r,1,beta,ltr,1)
          
c         1b. Initialise r: i.e. r = ltr
          call dcopy(m, ltr, 1, r, 1)
          
          if (pmiss(t).eq.0) then
              !data not missing
              beta = 1.0

c             1c. Compute: r = (s * nu) + r
              call dgemv('t',p,m,alpha,s(:,:,t),p,nu(:,t),1,beta,r,1)
          endif

c         Step 2: Compute ahat(t) = a(t) + P(t) * r(t-1)

c         2a. Initialise as: i.e. ah(:,t) = as(:, t)
          call dcopy(m, as(:,t), 1, ah(:,t), 1)
          
c         2b. Compute: ah = ah + ps*r
          beta = 1.0
          call dgemv('n',m,m,alpha, ps(:,:,t), m, r,1, beta, ah(:,t),1)
          
      enddo
      end

c ------------------------------------------------------------------

c     subroutine for smoothing. Standard state space model. Non time varying system matricies.
      subroutine ntsmoother(ah,s,nu,ls,r,ltr,as,ps,lt,p,m,n) 
      integer p,m,n,t,i,lt,it
      real*8 ah(m,n),s(p,m,n),nu(p,n),ls(m,m,n),r(m),ltr(m)
      real*8 as(m,n), ps(m,m,n)
      real*8 alpha, beta
c ----------------------
cf2py intent(inout) ah
cf2py intent(in) s
cf2py intent(in) nu
cf2py intent(in) ls
cf2py intent(in) r
cf2py intent(in) ltr
cf2py intent(in) as
cf2py intent(in) ps
cf2py intent(in) lt
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n
c ----------------------
c     Initialise vector
      do i = 1, m
          r(i) = 0.0
      enddo

      alpha = 1.0
      do t = n, 1, -1
      
          if (t.gt.lt) then
              it = lt
          else
              it = t
          endif

c         Step 1: Compute r(t-1) = S(t)'*nu(t) + L(t)'r(t)
          beta = 0.0
c         1a. Compute: ltr = ls * r     
          call dgemv('t',m,m,alpha,ls(:,:,it),m,r,1,beta,ltr,1)
c         1b. Initialise: r = ltr
          call dcopy(m,ltr,1,r,1)
c         1c. Compute: r = r + s * nu
          beta = 1.0
          call dgemv('t',p,m,alpha,s(:,:,it),p,nu(:,t),1,beta,r,1)
c         -----------------------------------------------
c         Step 2: Compute ahat(t) = a(t) + P(t)*r(t-1)
c         2. Initialise ah = as
          call dcopy(m,as(:,t),1,ah(:,t),1)
c         2b. Compute: ah = ah + ps * r          
          call dgemv('n',m,m,alpha,ps(:,:,it),m,r,1,beta,ah(:,t),1)
      enddo
      end

c ------------------------------------------------------------------

c     subroutine for state disturbance smoother
      subroutine dsmoother(ehat,nu,st,jt,rt,ls,ltr,pmiss,p,m,n,r)
      implicit none
      integer p, m, n, r, t, i, pmiss(n)
      real*8 nu(p,n), st(p,m,n), jt(r,m,n), rt(m), ls(m,m,n)
      real*8 alpha, beta, ehat(r,n), ltr(m)
c ----------------------
cf2py intent(in) nu
cf2py intent(in) st
cf2py intent(in) jt
cf2py intent(in) rt
cf2py intent(in) ls
cf2py intent(inout) ehat
cf2py intent(in) ltr
cf2py intent(in) pmiss
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n
cf2py intent(in) r
c ----------------------
c     Initialise rt array
      do i = 1, m
          rt(i) = 0.0
      enddo
      
      alpha = 1.0
      do t = n, 1, -1
      
c         1. Compute: ehat(t) = J(t) * rt
          beta = 0.0
          call dgemv('n',r,m,alpha,jt(:,:,t),r,rt,1,beta,ehat(:,t),1)
c         ---------------------------------------------
c         2.  Compute: r(t-1) = S(t)'.nu(t) + L(t)'.r(t)
          beta = 0.0
c         2a. Compute: ltr = ls(t)' * rt
          call dgemv('t',m,m,alpha,ls(:,:,t),m,rt,1,beta,ltr,1)
c         2b. Initialise: rt = ltr
          call dcopy(m,ltr,1,rt,1)
          beta = 1.0
          if (pmiss(t).eq.0) then
c             2c. Compute: rt = rt + st'.nu          
              call dgemv('t',p,m,alpha,st(:,:,t),p,nu(:,t),1,beta,rt,1)
          endif
      enddo
      end
      
c ------------------------------------------------------------------

c     subroutine for state disturbance smoother
      subroutine ntdsmoother(ehat,nu,st,jt,rt,ls,ltr,lt,p,m,n,r)
      implicit none
      integer p,m,n,r,lt,it,t,i
      real*8 nu(p,n),st(p,m,n),jt(r,m),rt(m),ls(m,m,n)
      real*8 alpha,beta,ehat(r,n),ltr(m)

c     NOTE: r(t) is input, used in calcs, then over written with r(t-1)
c ----------------------
cf2py intent(in) nu
cf2py intent(in) st
cf2py intent(in) jt
cf2py intent(in) rt
cf2py intent(in) ls
cf2py intent(inout) ehat
cf2py intent(in) ltr
cf2py intent(in) lt
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n
cf2py intent(in) r
c ----------------------
c     Initialise rt array
      do i = 1, m
          rt(i) = 0.0
      enddo

      alpha = 1.0
      do t = n, 1, -1
      
          if (t.gt.lt) then
              it = lt
          else
              it = t
          endif
c         --------------------------------
c         1. Compute: etahat = J(t)*r(t)
          beta = 0.0
          call dgemv('n',r,m,alpha,jt,r,rt,1,beta,ehat(:,t),1)
c         -----------------------------------------------
c         2. Compute: r(t-1) = S(t)'.nu(t) + L(t)'.r(t)
c         2a. Compute: ltr = ls'.rt
          beta = 0.0
          call dgemv('t',m,m,alpha,ls(:,:,it),m,rt,1,beta,ltr,1)
c         2b. Initialise: rt = ltr          
          call dcopy(m,ltr,1,rt,1)
          beta = 1.0
c         2c. Compute: rt = rt + st'.nu          
          call dgemv('t',p,m,alpha,st(:,:,it),p,nu(:,t),1,beta,rt,1)
      enddo
      end
      
c ------------------------------------------------------------------

c     subroutine calculates the Frobenius norm for the difference of two matrices
      real*8 function fnorm(a,b,m,n)
      implicit none
      integer m,n,i,j
      real*8 a(m,n), b(m,n), sumd

      sumd = 0.0
      do j = 1, n
          do i = 1, m
              sumd = sumd + (a(i,j)-b(i,j))**2
          enddo
      enddo
      fnorm = sqrt(sumd)
      return
      end
      
c ------------------------------------------------------------------

c     benchmark simulation smoothing routine
      subroutine bsmoother(ah,z,fi,fn,nu,ls,r,ltr,as,ps,p,m,n, n_z) 
      integer p,m,n,t,i, n_z, t_z, timet
      real*8 ah(m,n),z(p,m,n_z),fi(p,p,n),fn(p),nu(p,n),ls(m,m,n),r(m)
      real*8 as(m,n), ps(m,m,n),ltr(m)
      real*8 alpha, beta
c ----------------------
cf2py intent(inout) ah
cf2py intent(in) fi
cf2py intent(in) fn
cf2py intent(in) nu
cf2py intent(in) ls
cf2py intent(in) r
cf2py intent(in) ltr
cf2py intent(in) as
cf2py intent(in) ps
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n
cf2py intent(in) n_z
c ----------------------
      do i = 1,m
          r(i) = 0.0
      enddo

      alpha = 1.0
      do t = n, 1, -1
      
          t_z = timet(n_z, t)
      
c         r(t-1)=Z(t)'inv(F(t))*nu(t)+L(t)'r(t)
          beta = 0.0
          call dgemv('t',m,m,alpha,ls(:,:,t),m,r,1,beta,ltr,1)
          call dcopy(m,ltr,1,r,1)
          call dgemv('n',p,p,alpha,fi(:,:,t),p,nu(:,t),1,beta,fn,1)
          beta = 1.0
          call dgemv('t',p,m,alpha,z(:,:,t_z),p,fn,1,beta,ltr,1)
          call dcopy(m,ltr,1,r,1)
          
c         ahat(t)=a(t)+P(t)*r(t-1)
          call dcopy(m,as(:,t),1,ah(:,t),1)
          call dgemv('n',m,m,alpha,ps(:,:,t),m,r,1,beta,ah(:,t),1)
      enddo
      end

c ------------------------------------------------------------------

c     Procedure to initialise an identity matrix of specified dimension
      subroutine eye(a,m)
      integer m, i, j
      real*8 a(m,m)

      do i = 1, m
          do j = 1, m
              a(i,j) = 0.0
          enddo
          a(i,i) = 1.0
      enddo
      
      end
      
c ------------------------------------------------------------------

c     de Jong and Shephard simulation smoother
      subroutine dssimsm(eta,s,nu,z,w,u,ls,rt,nt,v,nl,jt,
     + ct,nj,lr,qt,ifo,pmiss,p,m,r,n, n_z, n_q)
      implicit none
      integer ifo,info,p,m,r,n,t,i,j, t_z, n_z, t_q, n_q, timet
      integer pmiss(n)
      real*8 eta(r,n),s(p,m,n),nu(p,n), z(p,m,n_z), w(r,m), u(r)
      real*8 ls(m,m,n),rt(m),nt(m,m),v(r,m),nl(m,m),jt(r,m,n)
      real*8 ct(r,r),nj(m,r),lr(m), qt(r,r,n_q)
      real*8 alpha,beta
c     on entry eta is a matrix of random normals on exit it is a
c     sample of eta
c ----------------------
cf2py intent(inout) eta
cf2py intent(in) s
cf2py intent(in) nu 
cf2py intent(in) z
cf2py intent(in) w
cf2py intent(in) u
cf2py intent(in) ls
cf2py intent(inout) rt
cf2py intent(in) nt
cf2py intent(in) v
cf2py intent(in) nl
cf2py intent(in) jt
cf2py intent(in) ct
cf2py intent(in) nj
cf2py intent(in) lr
cf2py intent(in) qt
cf2py intent(in) pmiss
cf2py intent(inout) ifo
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) r
cf2py intent(in) n
cf2py intent(in) n_z
cf2py intent(in) n_q
c ----------------------
      do j = 1, m
          rt(j) = 0.0
          do i = 1, m
              nt(i,j) = 0.0
          enddo
      enddo
          
      do t = n, 1, -1
      
          t_z = timet(n_z, t)
          t_q = timet(n_q, t)
          
          alpha = 1.0
          beta = 0.0
c          NL(t) = N(t) * L(t)
          call dgemm('n','n',m,m,m,alpha,nt,m,ls(:,:,t),m,beta,nl,m)

c         W(t) = J(t) * NL(t)
          call dgemm('n','n',r,m,m,alpha,jt(:,:,t),r,nl,m,beta,w,r)

c         NJ(t) = N(t) * J(t)'     
          call dgemm('n','t',m,r,m,alpha,nt,m,jt(:,:,t),r,beta,nj,m)

c         C(t) = Q(t)-J(t) * NJ(t)
          do i=1,r
              call dcopy(r,qt(:,i,t_q),1,ct(:,i),1)
          enddo
          alpha = -1.0
          beta = 1.0
          call dgemm('n','n',r,r,m,alpha,jt(:,:,t),r,nj,m,beta,ct,r)

c         C(t) * V(t) = W(t); solve for V(t) 
          do i = 1, m
              call dcopy(r,w(:,i),1,v(:,i),1)
          enddo
          
          call dposv('u',r,m,ct,r,v,r,info)
          if (info.ne.0) then
              ifo = 1
          endif
          
c          d(t)~N(0,C(t)); on exit eta(:,t) = d(t)
           call dtrmv('u','t','n',r,ct,r,eta(:,t),1)

c          C(t) * U(t) = d(t); solve for U(t)
           call dcopy(r,eta(:,t),1,u,1)
           call dtrsv('u','t','n',r,ct,r,u,1)
           call dtrsv('u','n','n',r,ct,r,u,1)

c          eta = d(t) + J(t) * r(t)
           alpha = 1.0
           beta = 1.0
           call dgemv('n',r,m,alpha,jt(:,:,t),r,rt,1,beta,eta(:,t),1)

c          r(t) = S(t)' * nu(t) - W(t)' * U(t) + l(t)'r(t)
           beta = 0.0
           call dgemv('t',m,m,alpha,ls(:,:,t),m,rt,1,beta,lr,1)
           call dcopy(m,lr,1,rt,1)
           alpha = -1.0
           beta = 1.0
           call dgemv('t',r,m,alpha,w,r,u,1,beta,rt,1)
           alpha = 1.0
           if (pmiss(t).eq.0) then
               call dgemv('t',p,m,alpha,s(:,:,t),p,nu(:,t),1,beta,rt,1)
           endif

c          N(t) = S(t)'Z(t) + W(t)'V(t) +L(t)'NL(t) 
           beta = 0.0
           call dgemm('t','n',m,m,m,alpha,ls(:,:,t),m,nl,m,beta,nt,m)
           beta = 1.0
           call dgemm('t','n',m,m,r,alpha,w,r,v,r,beta,nt,m)
           if (pmiss(t).eq.0) then
               call dgemm('t','n',m,m,p,alpha,s(:,:,t),p,z(:,:,t_z),p,
     + beta,nt,m)
           endif
       enddo
       end
       
c ------------------------------------------------------------------

c     de Jong and Shephard simulation smoother non time varying system
c     matricies
      subroutine ntdssimsm(eta,s,nu,z,w,u,ls,rt,nt,v,nl,jt,
     + ct,nj,lr,qt,lt,ifo,p,m,r,n)
      implicit none
      integer ifo,info,lt,it,p,m,r,n,t,i,j
      real*8 eta(r,n),s(p,m,n),nu(p,n),z(p,m),w(r,m),u(r)
      real*8 ls(m,m,n),rt(m),nt(m,m),v(r,m),nl(m,m),jt(r,m)
      real*8 ct(r,r),nj(m,r),lr(m),qt(r,r)
      real*8 alpha,beta
c     on entry eta is a matrix of random normals on exit it is a
c     sample of eta
c ----------------------
cf2py intent(inout) eta
cf2py intent(in) s
cf2py intent(in) nu 
cf2py intent(in) z
cf2py intent(in) w
cf2py intent(in) u
cf2py intent(in) ls
cf2py intent(inout) rt
cf2py intent(in) nt
cf2py intent(in) lt
cf2py intent(in) v
cf2py intent(in) nl
cf2py intent(in) jt
cf2py intent(in) ct
cf2py intent(in) nj
cf2py intent(in) lr
cf2py intent(in) qt
cf2py intent(inout) ifo
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) r
cf2py intent(in) n
c ----------------------
      do j = 1, m
          rt(j) = 0.0
          do i = 1, m
              nt(i,j) = 0.0
          enddo
      enddo
          
      do t = n, 1, -1
          if (t.lt.lt) then
              it = t
          else
              it = lt
          endif
          
          alpha = 1.0
          beta = 0.0
c     NL(t) = N(t) * L(t)
          call dgemm('n','n',m,m,m,alpha,nt,m,ls(:,:,it),m,beta,nl,m)
c     W(t) = J(t) * NL(t)
          call dgemm('n','n',r,m,m,alpha,jt,r,nl,m,beta,w,r)
c     NJ(t) = N(t) * J(t)'     
          call dgemm('n','t',m,r,m,alpha,nt,m,jt,r,beta,nj,m)
c     C(t) = Q(t)-J(t) * NJ(t)
          do i = 1, r
              call dcopy(r,qt(:,i),1,ct(:,i),1)
          enddo
          alpha = -1.0
          beta = 1.0
          call dgemm('n','n',r,r,m,alpha,jt,r,nj,m,beta,ct,r)
c     C(t) * V(t) = W(t); solve for V(t) 
          do i = 1, m
              call dcopy(r,w(:,i),1,v(:,i),1)
          enddo
          
          call dposv('u',r,m,ct,r,v,r,info)
          if (info.ne.0) then
              ifo = 1
          endif
c      d(t)~N(0,C(t)); on exit eta(:,t) = d(t)
           call dtrmv('u','t','n',r,ct,r,eta(:,t),1)
c      C(t) * U(t) = d(t); solve for U(t)
           call dcopy(r,eta(:,t),1,u,1)
           call dtrsv('u','t','n',r,ct,r,u,1)
           call dtrsv('u','n','n',r,ct,r,u,1)
c      eta = d(t) + J(t) * r(t)
           alpha = 1.0
           beta = 1.0
           call dgemv('n',r,m,alpha,jt,r,rt,1,beta,eta(:,t),1)

c      r(t) = S(t)' * nu(t) - W(t)' * U(t) + l(t)'r(t)
           beta = 0.0
           call dgemv('t',m,m,alpha,ls(:,:,it),m,rt,1,beta,lr,1)
           call dcopy(m,lr,1,rt,1)
           alpha = -1.0
           beta = 1.0
           call dgemv('t',r,m,alpha,w,r,u,1,beta,rt,1)
           alpha = 1.0
           call dgemv('t',p,m,alpha,s(:,:,it),p,nu(:,t),1,beta,rt,1)
c      N(t) = S(t)'Z(t) + W(t)'V(t) +L(t)'NL(t) 
           beta = 0.0
           call dgemm('t','n',m,m,m,alpha,ls(:,:,it),m,nl,m,beta,nt,m)
           beta = 1.0
           call dgemm('t','n',m,m,r,alpha,w,r,v,r,beta,nt,m)
           call dgemm('t','n',m,m,p,alpha,s(:,:,it),p,z,p,beta,
     + nt,m)
       enddo
       end
       
c ------------------------------------------------------------------

c      subroutine to update J(t) in the time varying case
       subroutine update_jt(jt,qt,gt,r,m,n, n_q, n_g)
       implicit none
       integer n,r,m,t, n_g, n_q, t_q, t_g, timet
       real*8 jt(r,m,n),qt(r,r,n_q),gt(m,r,n_g)
       real*8 alpha, beta      
c ----------------------
cf2py intent(inout) jt
cf2py intent(in) qt
cf2py intent(in) gt
cf2py intent(in) r
cf2py intent(in) m
c ----------------------
       alpha = 1.0
       beta = 0.0
       
c$omp parallel default(shared) private(t, t_g, t_q)
c$omp do schedule(static)     
       do t = 1, n       
          t_q = timet(n_q, t)
          t_g = timet(n_g, t)
       
c         Compute: j(t) = q(t) * g(t)' 
          call dgemm('n','t',r,m,r,alpha,qt(:,:,t_q),r,gt(:,:,t_g),
     + m, beta, jt(:,:,t),r)
       enddo
c$omp end do
c$omp end parallel
       end

c ------------------------------------------------------------------       

c **/** NEW OPENMP ADDED  - TESTED **/**

c      subroutine to calculate the state vector given the initial state
c      and the state disturbances
       subroutine genstate(eta,tt,gt,st,m,r,n, n_t, n_g)
       implicit none
       integer n,m,r,t, n_g, n_t, t_t, t_g, timet
       real*8 eta(r,n), tt(m,m,n_t), gt(m,r,n_g), st(m,n)
       real*8 alpha,beta
c ----------------------
cf2py intent(in) eta
cf2py intent(in) tt
cf2py intent(in) gt
cf2py intent(inout) st
cf2py intent(in) m
cf2py intent(in) r
cf2py intent(in) n_t
cf2py intent(in) n_g
c ----------------------
      alpha = 1.0
      beta = 0.0  
      
!  NON OPENMP VERSION:       
!        do t = 1, n-1                        
!          t_t = timet(n_t, t)                
!          t_g = timet(n_g, t)        
!          beta = 0.0
c          Compute: st(:,t+1) = tt . st(:,t)                
!          call dgemv('n',m,m, alpha, tt(:,:,t_t), m, st(:,t), 1,
!     + beta, st(:,t+1), 1)      
!          beta = 1.0   
c          Compute: st(:,t+1) = st(:,t+1) + gt * eta(:,t)                          
!          call dgemv('n',m,r,alpha,gt(:,:,t_g),m,eta(:,t),1,beta,
!     + st(:,t+1),1)    
!      enddo
              
! OPENMP VERSION: Re-ordering of tasks necessary
      beta = 0.0   
      
c$omp parallel default(shared) private(t, t_g)             
c$omp do schedule(static)
      do t = 1, n-1
          t_g = timet(n_g, t)
c         Compute: st(:,t+1) = gt * eta(:,t)                          
          call dgemv('n',m,r,alpha,gt(:,:,t_g),m,eta(:,t),1,beta,
     + st(:,t+1),1)
      enddo
c$omp end do
c$omp end parallel

      beta = 1
      
      do t = 1, n-1                
          t_t = timet(n_t, t)                
c         Compute: st(:,t+1) = st(:,t+1) + tt . st(:,t)                
          call dgemv('n',m,m, alpha, tt(:,:,t_t), m, st(:,t), 1,
     + beta, st(:,t+1), 1)      
      enddo                  
      
      end
      
c ------------------------------------------------------------------ 
        
c **/** NEW OPENMP ADDED  - TESTED **/**
        
c      subroutine to calculate the state vector given the initial state
c      and the state disturbances and non time varying system matricies
       subroutine ntgenstate(eta,tt,gt,st,m,r,n)
       implicit none
       integer n,m,r,t
       real*8 eta(r,n),tt(m,m),gt(m,r),st(m,n)
       real*8 alpha,beta
c ----------------------
cf2py intent(in) eta
cf2py intent(in) tt
cf2py intent(in) gt
cf2py intent(inout) st
cf2py intent(in) m
cf2py intent(in) r
cf2py intent(in) n
c ----------------------
      alpha = 1.0        
      beta = 0.0 
      
c$omp parallel default(shared) private(t)             
c$omp do schedule(static)
      do t = 1, n-1         
c         Compute: st(:,t+1) = gt * eta(:,t)                  
          call dgemv('n',m,r,alpha,gt,m,eta(:,t),1,beta,st(:,t+1),
     + 1)
      enddo
c$omp end do
c$omp end parallel      
     
      beta = 1.0 
      do t = 1, n-1        
c         Compute: st(:,t+1) = st(:,t+1) + tt . st(:,t)                 
          call dgemv('n',m,m,alpha,tt,m,st(:,t),1,beta,st(:,t+1),
     + 1)     
      enddo      
      
      end

c ------------------------------------------------------------------

c     subroutine returns the kernel for the log probability of the state
c      subroutine lnprst(pr,res,cqt,gcqt,r,n,nq,ngq,m)
      subroutine lnprst(pr,res,cqt,gqg,cgqg,w,wk,ifo,fl,lw,r,n,nq,ngq,m)
      implicit none
      integer r, m, n, t, nq, t_q, ngq, t_gq, timet, lw, ifo, fl
      real*8 res(r,n-1), cqt(r,r,nq), gqg(m,m,ngq), w(*)
      real*8 pr, alpha, ddot, gldet, wk(lw), cgqg(m,m), ldet
c ----------------------
cf2py intent(inout) pr
cf2py intent(in) res
cf2py intent(in) cqt
cf2py intent(in) r
cf2py intent(in) n
c ----------------------
      pr = 0.0
      alpha = 1.0

      if (fl.eq.0) then
          ldet = gldet(gqg(:,:,1),cgqg,w,wk,ifo,lw,m)
          
c$omp parallel default(shared) private(t, t_q, t_gq)
c$omp do reduction(-:pr)
          do t = 1, n-1
              t_q = timet(nq, t)
              t_gq = timet(ngq,t)
              call dtrsm('l','l','n','n',r,1,alpha,cqt(:,:,t_q),r,
     + res(:,t),r)
c          pr = pr-ddot(r,res(:,t),1,res(:,t),1)-glogdetchol(gcqt(:,:,
c     + t_gq),m,r)
              pr = pr - ddot(r,res(:,t),1,res(:,t),1) - ldet
          enddo
c$omp end do
c$omp end parallel

          pr = pr * 0.5

      else

c     need to modify for the case where ngq and nq eq 1
c$omp parallel default(shared) private(t, t_q, t_gq, cgqg, wk, ldet)
c$omp do reduction(-:pr)
          do t = 1, n-1
              t_q = timet(nq, t)
              t_gq = timet(ngq,t)
              call dtrsm('l','l','n','n',r,1,alpha,cqt(:,:,t_q),r,
     + res(:,t),r)
c          pr = pr-ddot(r,res(:,t),1,res(:,t),1)-glogdetchol(gcqt(:,:,
c     + t_gq),m,r)
              ldet = gldet(gqg(:,:,t_gq),cgqg,w,wk,ifo,lw,m)
              pr = pr - ddot(r,res(:,t),1,res(:,t),1) - ldet
          enddo
c$omp end do          
c$omp end parallel
          pr = pr * 0.5
      endif

      end

c -----------------------------------------------------------------

c     computes generalised log determinant of a matrix a where the 
c     generalised determinant is the sum of the log of the non zero
c     eigenvalues

      real*8 function gldet(a,ca,w,wk,ifo,lw,m)
      implicit none
      integer m,lw,i,ifo
      real*8 a(m,m), ca(m,m), w(m), wk(lw), tol
      
c	  tolerance
      tol = 1D-10
c     1. Initialise: ca = a      
      do i = 1, m
          call dcopy(m,a(:,i),1,ca(:,i),1)
      enddo

c     2. Compute: w = eigenvalues of ca
      call dsyev('n','u',m,ca,m,w,wk,lw,ifo)

c     3. Compute: determinant. Ignore zero values
      gldet = 0.0
      do i = 1, m
          if (w(i).gt.tol) then
              gldet = gldet + log(w(i))
          endif
      enddo
          
      return 
      end function gldet
      

c ------------------------------------------------------------------

c     simulation smoother of Fruwirth  Snatter(1994) and Carter and
c     Kohn(1994) to simulate the state
      subroutine fscksimsm(st, as, pt, at, wt, ps, ab, pb, rs, wk,
     + ifo, lt, m, n)
      implicit none
      integer ifo, m, n, t, info, i, lt, it
      real*8 st(m,n), as(m,n+1), at(m,n), pt(m,m,n), wt(m,m,n)
      real*8 ps(m,m,n+1), pb(m,m), rs(m), alpha, beta, wk(m,m), ab(m)
c ----------------------
cf2py intent(inout) st
cf2py intent(in) as
cf2py intent(in) pt
cf2py intent(in) at
cf2py intent(in) wt
cf2py intent(in) ps
cf2py intent(in) ab
cf2py intent(in) pb
cf2py intent(in) rs
cf2py intent(in) wk
cf2py intent(inout) ifo
cf2py intent(in) m
cf2py intent(in) n
cf2py intent(in) lt
c ----------------------      
c     Note: On exit st is the state. On entry st is a matrix of random numbers
c     Note: pb on entry should equal P(n|n). pb is then used to store pbar(t)
c     Note: ab on entry should equal a(n|n)
c     Note: ps is abrev for pstore
c     Note: pt, at equivalent to p(t|t) & a(t|t) (i.e. pt_t & at_t)
c     Note: ab used to store a(n|n)
c     Note: as used to store a(t)

c     Note: lt used to differentiate between time varying & non time (nt) varying situation
c     Note: lt = time of steady state occurrence. No results stored after this time in nt version

c     1. Compute cholesky factorization of P(n|n) ( == L.L^T). Assign as pb
      call dpotrf('u', m, pb, m, info)
      if (info.ne.0) then
          ifo = 1
          print *, 'Erorr: Failed to solve [fscksimsm:1]'
      endif

c     Sampling step part 1:  In general alpha = a(n|n) + L.randval where L = pb^T
c     2. Compute: st(:,n) = pb^T * st(:,n) where pb is upper triangular
      call dtrmv('u','t','n', m, pb, m, st(:,n), 1)
              
c     Sampling step part 2: Add mean a(n|n)
c     3. Compute: st(:,n) = st(:,n) + alpha * ab 
      alpha = 1.0
      call daxpy(m, alpha, ab, 1, st(:,n), 1)        
    
      do t = n-1, 1, -1
      
          if (t.gt.lt) then
              it = lt
          else
              it = t
          endif
      
c         Initialise pb as P(t|t)
          do i = 1, m          
              call dcopy(m, pt(:,i,t), 1, pb(:,i), 1)
          enddo

c         4. abar(t) calc      
c         Compute: rs = st(:,t+1) - as(:,t)
          do i = 1, m
              rs(i) = st(i,t+1) - as(i,t)
          enddo

c         5. Compute P(t)^-1 * (alpha(t+1) - a(t))  == ps^-1 * rs
c         i.e. Solve ps * x = rs where ps is upper triangular
c         On exit: rs = inv(ps) * rs
          call dposv('u', m, 1, ps(:,:,it), m, rs, m, info)
          if (info.ne.0) then
              ifo = 1
              print *, 'Error: Failed to solve [fscksimsm:5]'
          endif

c         6. Initialise abar(t), i.e assign ab = at(:,t)
          call dcopy(m, at(:,t), 1, ab, 1)
          
c         7. abar(t) calc: final part, put everything together
c         Update: ab = ab + wt(:,:,t) * rs
          alpha = 1.0
          beta = 1.0
          call dgemv('n',m,m, alpha, wt(:,:,it), m, rs, 1, beta, ab, 1)

c         8. Make a copy: wk = wt(:,:,t)          
          do i = 1, m
              call dcopy(m, wt(:,i,it), 1, wk(:,i), 1)
          enddo

c         9. Split P(t)^-1 into L. L^T => (W(t).L^-T) * (L^-1. W(t)^T)
c         Compute: W(t) .L^-T == wk .L^-T  == y
c         i.e. Solve y .L = wk;  Note: wk = y on exit         
          call dtrsm('r','u','n','n', m, m, alpha, ps(:,:,it), m, wk, m)

c         10. Update: pb = pb - wk * wk^T 
          alpha = -1.0
          beta = 1.0
          call dgemm('n','t',m,m,m, alpha, wk, m, wk, m, beta, pb, m)
          
c         11. Compute cholesky factorization of matrix 'pb'          
          call dpotrf('u', m, pb, m, info)
          if (info.ne.0) then
              ifo = 1
              print *, ifo, 'Error: Failed to solve [fscksimsm:11]'
              print *, 'pb = ', pb(1,:)
              print *, 'pb = ', pb(2,:)
              print *,t              
              stop
          endif

c         12. Compute: st(:,t) = pb^T * st(:,t) where pb is upper triangular
c         i.e. st(:,n) = chol(pb) * st(:,t) 
          call dtrmv('u','t','n', m, pb, m, st(:,t), 1)
             
c         13. Compute: st(:,t) = st(:,t) + alpha * ab 
          alpha = 1.0
          call daxpy(m, alpha, ab, 1, st(:,t), 1)
      enddo
      
      end
          
! -------------------------------------------------------------------

c     subroutine returns the kernel for the log probability of the state
c     non-time varying system matricies
      subroutine ntlnprst(pr,res,cqt,r,n)
      implicit none
      integer r,n,t
      real*8 res(r,n),cqt(r,r)
      real*8 pr,alpha,ddot,logdetchol
c ----------------------
cf2py intent(inout) pr
cf2py intent(in) res
cf2py intent(in) cqt
cf2py intent(in) r
cf2py intent(in) n
c ----------------------
      pr = 0.0
      alpha = 1.0

      call dtrsm('l','l','n','n',r,n,alpha,cqt,r,res,r)
      do t = 1, n
          pr = pr + ddot(r,res(:,t),1,res(:,t),1)
      enddo
      pr = -0.5*pr
      end
      
c ------------------------------------------------------------------          

c     subroutine calculates the log determinant from the cholesky decompsion
c     of a matrix.  
      real*8 function logdetchol(ch,m)
      implicit none
      integer m,i
      real*8 ch(m,m)

      logdetchol = 0.0
      do i = 1, m
          logdetchol = logdetchol + log(ch(i,i))
      enddo
      logdetchol = 2.0*logdetchol
      end
      
c ------------------------------------------------------------------         

c     subroutine calculates the log determinant for gqg. This is really
c     a generalised determinant as gqg does not need to be positive
c     definite. Instead we need the determinant for the parts of gqg for
c     which the diagonal is not zero


      real*8 function glogdetchol(gcqt,m,r)
      implicit none
      integer m,r,i
      real*8 gcqt(m,r),alpha

      glogdetchol = 0.0
      do i = 1, r
          if (gcqt(i,i).eq.0.0) then
              alpha = 0.0
          else
              alpha = log(gcqt(i,i))
          endif

          glogdetchol = glogdetchol + alpha
      enddo
      glogdetchol = 2.0*glogdetchol
      end

c ------------------------------------------------------------------
      
      subroutine printm(a,m,n)
      implicit none
      integer m,n,i,j
      real*8 a(m,n)

      do i = 1, m
          write(*,*) (a(i,j),j=1,n)
      enddo
      end
      
c ------------------------------------------------------------------
      
      subroutine setflag(info, ifo)
      implicit none
      integer info, ifo
      
      if (info.ne.0) then
            ifo = ifo + 1
c           ifo = 1  (Optional)
      endif
      end


c ======================================================================
c      PARALLELISABLE "NONAME" SIMSM CODE BELOW
c ======================================================================

c     code to initialise a matrix with zeros
      subroutine initm(a,m,n)
      implicit none
      integer i, j, m, n
      real*8 a(m,n)
c$omp parallel default(shared) private(i,j)
c$omp do schedule(static)      
      do i = 1, m
          do j = 1, n
              a(i,j) = 0.0
          enddo
      enddo
c$omp end do      
c$omp end parallel      
      end
      
c ----------------------------------------------------------------------

c     Make a copy of the transpose of a matrix, i.e. set b = a'
      subroutine mcopytr(a, b, m, n)
      implicit none
      integer m, n, j
      real*8 a(m,n), b(n,m)                  
c$omp parallel default(shared) private(j)
c$omp do schedule(static)       
      do j = 1, n
c         Compute: b(j,i) = a(i,j) forall i 
          call dcopy(m,a(:,j),1,b(j,:),1)                           
      enddo
c$omp end do      
c$omp end parallel      
      end      
          
c ----------------------------------------------------------------------

c     Make a copy of a matrix, i.e. set b(i,j) = a(i,j) forall (i,j)
      subroutine mcopy(a, b, m, n)
      implicit none
      integer m, n, j
      real*8 a(m,n), b(m,n)
c$omp parallel default(shared) private(j)
c$omp do schedule(static)              
      do j = 1, n          
c         Compute: b(i,j) = a(i,j) forall i
          call dcopy(m, a(:,j), 1, b(:,j), 1)
      enddo 
c$omp end do      
c$omp end parallel                         
      end       
      
c ---------------------------------------------------------------------

c     Matrix plus matrix, i.e. b(i,j) = b(i,j) + a(i,j)
      subroutine mplusm(a, b, m, n)
      implicit none
      integer m, n, j
      real*8 a(m,n), b(m,n), alpha

      alpha = 1.0 
c$omp parallel default(shared) private(j)
c$omp do schedule(static) 
      do j = 1, n      
          call daxpy(m, alpha, a(:,j), 1, b(:,j), 1)     
      enddo  
c$omp end do      
c$omp end parallel      
      end 
      
c ----------------------------------------------------------------------  
    
c     Matrix plus matrix, i.e. c(i,j) = a(i,j) + b(i,j) forall (i,j)
      subroutine mplusm2(a, b, c, m, n)
      implicit none
      integer m, n, j 
      real*8 a(m,n), b(m,n), c(m,n), alpha
       
      alpha = 1.0
c$omp parallel default(shared) private(j)
c$omp do schedule(static)       
      do j = 1, n
c         Compute: c(:,j) = a(:,j)
          call dcopy(m, a(:,j), 1, c(:,j), 1)
c         Compute: c(:,j) = c(:,j) + b(:,j)
          call daxpy(m, alpha, b(:,j), 1, c(:,j), 1)
      enddo 
c$omp end do 
c$omp end parallel 
      end
      
c ----------------------------------------------------------------------

c     This procedure computes gqg as:  gqg =  gt_i'.inv[qt].gt_i

      subroutine compute_gqg(qt_type, gt_type, qt, gt_i, gqg, m,r, ifo)
      implicit none
      integer m, r, qt_type, gt_type, info, ifo
      real*8 gqg(m,m), alpha, beta
      real*8 qt(r,r), qtcopy(r,r) 
      real*8 gt_i(r,m), gt_i_copy(r,m), temp(m,r)
      
      alpha = 1.0
      beta = 0.0
      ifo = 0
     
      if(gt_type.eq.1) then ! gt is an identity matrix      
c Assert (r == m )
                
          if(qt_type.eq.3) then  ! qt is the inverse of qt               
               call mcopy(qt, gqg, m, m)  ! gqg = qt
          else
          
              call eye(gqg,m) ! Initialise gqg as Im
          
              if(qt_type.eq.4) then! qt is the cholesky factorisation of qt
                  ! Compute inv[Q] by solving Q. inv[Q] = I
                  alpha = 1.0                                
                  call dtrsm('l','l','n','n',r,r,alpha,qt,r,gqg,m)
              else ! qt is not a special case
                  call mcopy(qt, qtcopy,r,r)  ! qtcopy = qt
c                 Compute: gqg = inv[Q], i.e. solve: Q.inv[Q] = I
                  call dposv('u',r,m,qtcopy,r,gqg,m,info)
                  call setflag(info, ifo)
              endif
          endif  
c     -----------------------------------------------               
      else  ! i.e. gt_type != 1 and G is not an identity matrix
                
          if(qt_type.eq.1) then  ! qt is an identity matrix
c               Compute: gqg = gt_i'.gt_i  [i.e. (m,r) x (r,m)]
                call dgemm('t','n', m, m, r, alpha, gt_i, m, gt_i, m,
     + beta, gqg, m)
   
          elseif(qt_type.eq.3) then  ! input qt is the inverse of qt                        
c             Compute: temp = gt_i' * qt   &  gqg = temp * gt_i          
              call dgemm('t','n', m, r, r, alpha, gt_i, r, qt, r,
     + beta, temp, m)
              call dgemm('n','n', m, m, r, alpha, temp, m, gt_i, m,
     + beta, gqg, m)
                  
          elseif(qt_type.eq.4) then  ! input qt is the chol fact of qt                    
                            
              call mcopy(gt_i, gt_i_copy,r,m)  ! gt_i_copy = gt_i                
c             a. Compute: inv[qt].gt_i by solving qt.x = gt_i            
              call dtrsm('l','l','n','n', r, m, alpha, qt,
     + r, gt_i_copy, r)                                
c             b. Compute gqg = gt_i'.x                
              call dgemm('t','n', m, m, r, alpha, gt_i, r, gt_i_copy,
     + r, beta, gqg, m)
     
          else                         
c               Compute: qt_i = inv[G]'.inv[Q].inv[G]                                
c               Note: inv[G]'.inv[Q].inv[G] = inv[G]'.inv[L.L'].inv[G]
c                                           = inv[G]'.inv[L'].inv[L].inv[G]
c                                           = (inv[L].inv[G])'.(inv[L].inv[G])
c                                           = x'.x where x = inv[L].inv[G]               
            
c               a. Compute cholesky decomposition of qt, i.e. of qtcopy                     
                call mcopy(qt, qtcopy, r, r)  ! qtcopy = qt
                call dpotrf('l', r, qtcopy, r, info)
                call mcopy(gt_i, gt_i_copy,r,m)  ! gt_i_copy = gt_i           
                        
! POTENTIAL ERROR? ZERO UPPER PART OF gt_i_copy?                        
                                    
c               b. Solve: L.x = inv[G]                
                call dtrsm('l','l','n','n', r, m, alpha, qtcopy,
     + r, gt_i_copy, r)                    
                                          
c               c. Compute: gqg = x'.x
                call dgemm('t','n', m, m, r, alpha, gt_i_copy, 
     + r, gt_i_copy, r, beta, gqg, m)
                         
          endif        
      endif      
      
      if(ifo.gt.0) print *, 'Error: Failed to solve [compute_gqg]' 
      end

c ----------------------------------------------------------

c     Compute: z_h = Z'.inv[H]
      subroutine compute_zh(ht_type, ht, zt, z_h, p, m, n_p)
      implicit none
      integer p, m, ht_type, info, j, n_p
      real*8 htcopy(p,p), ht(p,n_p), zt(p,m), z_h(m,p), alpha, beta
                
      call mcopytr(zt, z_h, p, m)  ! z_h = zt'  
           
      ! Note: if(ht_type.eq.1) then do nothing      
      if(ht_type.eq.2) then  ! diagonal matrix                                                                          

c$omp parallel default(shared)
c$omp do schedule(static) private(j, alpha)     
          do j = 1, p   ! Iterate through columns of z_h             
              alpha = 1.0 / ht(j,1)
c             Compute: z_h(:,j) = alpha *z_h(:,j) 
              call dscal(m, alpha, z_h(:,j), 1)  
          enddo                                
c$omp end do      
c$omp end parallel 

      elseif(ht_type.eq.3) then! ht is the inverse of ht                
                        
          alpha = 1.0
          beta = 0.0
c         Compute: z_h = Z'* ht          
          call dgemm('t','n',m,p,p,alpha, zt, p, ht, p, beta, z_h, m)
           
      elseif(ht_type.eq.4) then ! ht is the cholesky fact of ht                                              
          
c         Compute: z_h = Z' * ht_i  by solving for z_h in z_h * ht = Z'
          alpha = 1.0                                
          call dtrsm('r','l','n','n',m,p,alpha,ht,p,z_h,m)
      
      else  ! None of the above special cases                                       
          
          call mcopy(ht,htcopy,p,p)  ! htcopy = ht
c         Compute cholesky decomposition of htcopy:     
          call dpotrf('l', p, htcopy, p, info)      
         
          if(info.gt.0) print *, 'Error: Failed to solve [compute_zh]'
          
c         Compute: z_h = Z' * ht_i  => Solve for z_h in z_h * ht = Z'
          alpha = 1.0                                
          call dtrsm('r','l','n','n',m,p,alpha,htcopy,p,z_h,m) 
      endif
            
      end
      
c -----------------------------------------------------------  

c     Compute: z_h_z = z_h * z    if beta = 0.0
c     OR z_h_z += z_h * z   if beta = 1.0 
      subroutine compute_zhz(zt_type, z_h, zt, z_h_z, beta, m, p)
      implicit none
      integer zt_type, m, p
      real*8 z_h_z(m,m), z_h(m,p), zt(p,m), alpha, beta
      
      alpha  = 1.0      
      if(zt_type.eq.1) then  ! zt is an identity matrix
!Assert (p == m)      
          if(beta.eq.0.0) then
              call mcopy(z_h, z_h_z, m, m)  ! z_h_z = z_h          
          else 
              call mplusm(z_h, z_h_z, m, m)! z_h_z = z_h_z + z_h
          endif
      else ! zt is not an identity matrix. Do multiplication                    
          call dgemm('n','n',m,m,p,alpha,z_h,m,zt,p,beta,z_h_z,m)
      endif         
      end
      
c --------------------------------------------------------------    
    
c     Compute: tgqgt = T'.gqgt  if beta = 0.0
c     OR tgqgt += T'.gqgt if beta = 1.0 
      subroutine compute_tgqgt(tt_type, tt, gqgt, tgqgt, beta, m)
c     Note: temp may be initialised as temp = z_h_z
      implicit none
      integer tt_type, m
      real*8 tgqgt(m,m), gqgt(m,m), tt(m,m), alpha, beta
      
      alpha  = 1.0            
      if(tt_type.eq.1) then  ! is an identity matrix                                  
                            
          if(beta.eq.0.0) then
              call mcopy(gqgt, tgqgt, m, m)  ! tgqgt = gqgt          
          else 
              call mplusm(gqgt, tgqgt, m, m)! tgqgt += gqgt
          endif                    
          
      else ! not identity matrix. Do multiplication          
          call dgemm('t','n',m,m,m,alpha,tt,m,gqgt,m,beta,tgqgt,m)
      endif
  
      end
      
c ------------------------------------------------------------ 

c     Procedure to calculate the pseudo inverse of a rectangular matrix
      subroutine compute_pseudoinv(mat, pinv, m, r, lwk)
      implicit none
      integer r, m, i, j, k, info, lwk
      real*8 mat(m,r), smat(m,r), pinv(r,m), alpha, beta
      real*8 umat(m,m), vtmat(r,r), v_si(r,m)
      real*8 wk(lwk), tol 

cf2py intent(in) mat
cf2py intent(inout) pinv
cf2py intent(in) m
cf2py intent(in) r
cf2py intent(in) lwk

c     Note: SVD of matrix A is A = U.S.V' where S is diagonal
c     Note: pinv = inv[A] = V.inv[S].U'    
c     Note: |inv[S]| = rxm. 
c     Note: To get inv[S] take recipricols of diagonals (and transpose)       
      
      tol = 0.00000001

c     Compute singular value decomposition:
      call dgesvd('a','a',m, r, mat, m, smat, umat, m, vtmat, r, 
     + wk, lwk, info)
 
      if(info.gt.0) print *, 'Error: SVD failed [compute_pseudoinv]'
 
c     Compute: v_si = v.inv[S]    i.e. (r,m) = (r,r) * (r,m)
      k = min(m,r)
      
c$omp parallel default(shared) private(alpha, i, j) 
c$omp do schedule(static)    
      do j = 1, k          
          alpha = 0.0
          ! Check whether smat(j,j) is zero or not
          ! otherwise recipricol will be infinity
          if(smat(j,j).gt.tol) then
              alpha = 1.0 / smat(j,j)
          endif
          
          ! Row j of vtmat becomes column j. Multiply elements by alpha. 
          do i = 1, r
              v_si(i,j) = alpha * vtmat(j,i)
          enddo        
      enddo 
c$omp end do

      ! Zero remaining columns
c$omp do schedule(static)
      do j = k+1, m
          do i = 1, r
              v_si(i,j) = 0.0
          enddo
      enddo
c$omp end do      
c$omp end parallel
                      
c     Compute: pinv = v_si * u',   (r,m) = (r,m) * (m,m)
      alpha = 1.0
      beta = 0.0
      call dgemm('n','t', r, m, m, alpha, v_si, r, umat,
     + m, beta, pinv, r)    

      end
      
c -----------------------------------------------------------

c     This procedure converts the diagonal and below diagonal blocks 
c     to the banded matrix storage scheme. 
      subroutine update_bands(bmat, block1, block2, t, m, two_m, mn)
      implicit none
      integer i, j, t, m, st, en, jstar, two_m, mn
      real*8 bmat(two_m, mn)
      real*8 block1(m,m), block2(m,m)
      
      jstar = (t-1)*m    
c$omp parallel default(shared) private(j, i, st, en)
c$omp do schedule(static)       
      do j = 1, m    ! Iterate through columns of the t-th block         
          st = 1
          en = 1 + m - j ! One element less per column
          bmat(st:en, jstar + j) = block1(j:m, j) ! Copy below diagonal only
          
          st = en + 1
          en = st + m - 1

          ! Copy all of block2. i.e. bmat(st:en, jstar + j) = - block2(:, j)            
          do i = 1, m
              bmat(st + i - 1, jstar + j) = -1 * block2(i,j)
          enddo
          
          ! Add zeros at the end of the column. Reason:
          ! 1) band continues outside block, OR
          ! 2) subdiagonal band has fewer elements than main diagonal
          do i = en+1, two_m
              bmat(i, jstar + j) = 0.0              
          enddo
      enddo 
c$omp end do      
c$omp end parallel
      end
      
c -----------------------------------------------------------------      

c     This procedure converts the last block to the banded matrix storage scheme
      subroutine finalise_bands(bmat, block, t, m, two_m, mn) 
      implicit none
      integer t, m, st, en, jstar, i, j, two_m, mn
      real*8 bmat(two_m, mn)
      real*8 block(m,m)
      
      jstar = (t-1)*m
      
c$omp parallel default(shared) private(i, j, st, en)
c$omp do schedule(static)      
      do j = 1, m  ! Iterate through columns of the t-th block          
          st = 1
          en = 1 + m - j
          bmat(st:en, jstar + j) = block(j:m, j)  ! Copy below diagonal only 
          
          ! Add zeros at the end of the column. Reason:
          ! 1) band continues outside block, OR
          ! 2) subdiagonal band has fewer elements than main diagonal
          do i = en+1, two_m
              bmat(i, jstar + j) = 0.0              
          enddo
      enddo
c$omp end do      
c$omp end parallel      
      end      
         
c -----------------------------------------------------------------

      subroutine convert_banded(bmat, dense, m, n, sym)    
c     Input: bmat is a lower triangular banded matrix in special structure     
c     Output: dense is a copy of bmat in std matrix format
c     Note: dense is symmetric
      implicit none
      integer b, i, j, m, n, sym
      real*8 bmat(m, n), dense(n,n)

c$omp parallel default(shared) private(i, j, b)   
c$omp do schedule(static)  
      do i = 1, n
          do j = 1, n
              dense(i,j) = 0.0
          enddo
      enddo
c$omp end do
                   
c$omp do schedule(static)                    
      do b = 1, m  ! For band b      
          do j = 1, n + 1 - b  ! For jth element in band b
              dense(b - 1 + j, j) = bmat(b, j)            
          enddo
      enddo
c$omp end do    
            
      if (sym.eq.1) then
c$omp do schedule(static) 
          do b = 1, m  ! For band b      
              do j = 1, n + 1 - b  ! For jth element in band b
                  dense(j, b - 1 + j) = bmat(b,j)  ! Symmetric component 
              enddo
          enddo
c$omp end do    
      endif        
      
c$omp end parallel       
      end      
      
c --------------------------------------------------------------      

c     Sampling procedure, i.e. state ~ Nc(bmat.mu, bmat) = N(mu, inv[bmat])
      subroutine sample_state(bmat, mu, state, mn, two_m)
      implicit none
      integer info, mn, two_m
      real*8 bmat(two_m, mn), dense(mn,mn)      
      real*8 state(mn), mu(mn), alpha
                     
      info = 0
                     
c     Solve: bmat.mu = rhs where rhs is recorded in variable mu initially
c     Note: bmat overwritten with cholesky decomposition, i.e.  matrix L
      call dpbsv('l', mn, two_m-1, 1, bmat, two_m, mu, mn, info)

      if(info.gt.0) then
          print *, info, 'Error: Failed to sovlve [sample state]'
          print *, 'bmat =', bmat(1, :5)
          print *, 'bmat =', bmat(2, :5)
          print *, 'bmat =', bmat(3, :5)
          print *, 'bmat =', bmat(4, :5)
          
          call convert_banded(bmat, dense, two_m, mn, 1)
          print *, dense(1,:6)
          print *, dense(2,:6) 
          print *, dense(3,:6)
          print *, dense(4,:6)
          stop
      endif
                      
c     Sampling step compute: sta = mu + inv[L'].randval
c     a. Set x = inv[L'].randval => L'.x = sta => Solve for x
c     Note: sta overwritten with x        
      call dtbsv('l','t','n', mn, two_m - 1, bmat, two_m, state, 1) ! original code
         
c     b. Compute: sta = mu + x, i.e. sta = sta + mu
      alpha = 1.0
      call daxpy(mn, alpha, mu, 1, state, 1)

      end
      
c ----------------------------------------------------------------------

c     Non time varying version of noname sim smoother             
      subroutine nt_noname_simsm(dense, rhs, sta, y, tt, ht, zt,
     + qt, gt_i, p1, a1, ht_type, zt_type, qt_type, gt_type, tt_type, 
     + ifo, two_m, mn, m, n, p, r, n_p)
     
c     Special: Calcs altered when zt, ht, qt, tt are special matrices      
c     Note: nseries stored as p; nstate stored as m
c     Note: nobs stored as n; rstate stored as r
c     Note: T stored as tt;  P(1) stored as p1
c     Note: Q stored as qt;  Z stored as zt
c     Note: inv[G] stored as gt_i;  H stored as ht 
c     Note: a(1) stored as a1; y(t) stored as yt
c     Note: On exit sta is the state vector. 
c     Note: On entry sta is a vector of random numbers

      implicit none      

      integer m, n, p, r, ifo, info, mn, two_m, t, st, n_p
      integer ht_type, qt_type, gt_type, tt_type, zt_type
      real*8 tt(m,m), ht(p,n_p), zt(p,m), qt(r,r), gt_i(r,m), z_h(m,p)
      real*8 p1(m,m), a1(m), y(p,n), alpha, beta
      real*8 sta(mn)
      real*8 gqg(m,m), gqgt(m,m)
      real*8 temp(m,m), diag_1(m,m), diag_2(m,m), diag_3(m,m)
      real*8 mu(mn), p1_i(m,m), p1copy(m,m)            
      real*8 bmat(two_m, mn)
      real*8 dense(mn,mn), lblock(m,m), rhs(mn)
c ----------------------    
cf2py intent(in) y
cf2py intent(in) tt
cf2py intent(in) ht
cf2py intent(in) zt
cf2py intent(in) qt
cf2py intent(in) gt_i
cf2py intent(in) p1
cf2py intent(in) a1
cf2py intent(in) ht_type
cf2py intent(in) qt_type
cf2py intent(in) gt_type
cf2py intent(in) tt_type
cf2py intent(in) zt_type
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n
cf2py intent(in) r
cf2py intent(in) n_p
cf2py intent(in) mn
cf2py intent(in) two_m
cf2py intent(inout) ifo
cf2py intent(inout) sta
cf2py intent(inout) dense
cf2py intent(inout) rhs
c ----------------------
      alpha = 1.0
      beta = 0.0          
c     ------------------------------------------------------------------
c$omp parallel default(shared)
c$omp sections
c$omp section
c     Compute: p1_i = inv(p1) => Solve p1 * p1_i  = I
      call eye(p1_i, m)  ! Initialise as identity , i.e. p1_i = Im     
c$omp section
c     Make a copy: p1copy = p1
      call mcopy(p1, p1copy, m, m)      
c$omp end sections
     
c     Wait for the above to be completed

c$omp single
c     Now do solve; Note: p1copy overwritten
      call dposv('u',m,m,p1copy,m,p1_i,m,info)         
      call setflag(info, ifo)                 
      
      if(info.gt.0) print *, 'Error: Failed to solve [nt_noname_simsm]'
c$omp end single  
        
c     ------------------------------------------------------------------
      
c$omp sections
c$omp section
c     Compute: z_h = Z'.inv[H]
      call compute_zh(ht_type, ht, zt, z_h, p, m, n_p)
c     ------------------------------------------------------------------
c$omp section
c     Compute: gqg  = inv[G]'.inv[Q].inv[G]   
      call compute_gqg(qt_type, gt_type, qt, gt_i, gqg, m, r, ifo)
c     ------------------------------------------------------------------
c     Compute: gqgt = gqg * T;                
      if(tt_type.eq.1) then ! is an identity matrix
          call mcopy(gqg, gqgt, m, m)
      else  ! not identity matrix
          call dgemm('n','n',m,m,m,alpha,gqg,m,tt,m,beta,gqgt,m)    
      endif         
c     ------------------------------------------------------------------
c$omp end sections

c     Wait for the above to be completed

c$omp single
c     Compute: temp = z_h * Z
      beta = 0.0
      call compute_zhz(zt_type, z_h, zt, temp, beta, m, p)        
      call mcopy(temp, diag_3, m,m) ! Set diag_3 = temp
c     ------------------------------------------------------------------      
c     Compute: temp += T'.gqgt 
      beta = 1.0
      call compute_tgqgt(tt_type, tt, gqgt, temp, beta, m)      
c$omp end single

c     Wait for the above to be completed

c     diag_1 and diag_2 calcs: 
c$omp sections
c$omp section
      call mplusm2(temp, p1_i, diag_1, m, m)  !  diag_1 = temp + p1_i    
c$omp section      
      call mplusm2(temp, gqg, diag_2, m, m)   !  diag_2 = temp + gqg          
c$omp section      
      call mplusm(gqg, diag_3, m, m)          !  diag_3 += gqg      
c$omp end sections 
    
c     -----------------------------------------------------------------    
c$omp single
c     Compute: mu
      t = 1
c     Compute: mu = z_h * y  (  == z_h_y)
      beta = 0.0
      call dgemv('n', m, p, alpha, z_h, m, y(:,1), 1, beta, mu(1:m), 1)
      
c     Compute: mu = mu + p1_i * a1  
      beta = 1.0
      call dgemv('n',m,m,alpha, p1_i, m, a1, 1, beta, mu(1:m), 1)
                 
      beta = 0.0
      !st = m + 1  Use code when run sequentially
c$omp end single
c     ------------------------------------------------------------------      
c$omp do schedule(static) private(t, st)   
      do t = 2, n                            
      
          st = (t-1)*m + 1 ! Use code when run in parallel
          
c         Compute: mu = z_h * y(t)  (  == z_h_y)          
          call dgemv('n', m, p, alpha, z_h, m, y(:,t), 1, beta,
     + mu(st:st + m - 1), 1)                                   
          
          !st = st + m   ! Use code when run sequentially 
      enddo
c$omp end do      
c     ------------------------------------------------------------------       
      call mcopy(gqgt, lblock, m, m)  ! Set lblock = gqgt
      
c$omp single
c     Build banded matrix:  (Copy column vectors from block matrices)
      t = 1        
      call update_bands(bmat, diag_1, lblock, t, m, two_m, mn)      
c$omp end single
c     ------------------------------------------------------------------
c$omp do schedule(static) private(t)
      do t = 2, n-1             
          call update_bands(bmat, diag_2, lblock, t, m, two_m, mn)
      enddo   
c$omp end do             
c$omp end parallel       
      t = n
      call finalise_bands(bmat, diag_3, t, m, two_m, mn)             
c     -----------------------------------------------------------      
      ! Debugging only: Remove from code completely
      call convert_banded(bmat, dense, two_m, mn, 1)
      call dcopy(mn, mu, 1, rhs, 1)  ! rhs = mu                        
c     --------------------------------------------------------------      
c     Sample state from ~ N(mu, inv[bmat])            
      call sample_state(bmat, mu, sta, mn, two_m)   ! banded matrix input                      
      end

c ------------------------------------------------------------------
      
c     Procedure determines index of time varying system matrix       
      integer function timet(n, t)
      implicit none
      integer n, t
c     Choose t th matrix or first. n > 1 => time varying
      timet = 1
      if(n.gt.1) then 
          timet = t      
      endif     
      return 
      end function timet
      
c ------------------------------------------------------------------

c     Time varying (non parallel) version of noname smoother
      subroutine tv_noname_simsm(sta, y, tt, ht, zt, qt, gt, p1,
     + a1, ht_type, zt_type, qt_type, gt_type, tt_type, ifo, two_m, mn,
     + m, n, p, r, n_t, n_h, n_z, n_q, n_g, n_p)
     
      implicit none
c     Note: Calcs altered when zt, ht, qt, tt are be identity matrices      
c     Note: nseries stored as p; nstate stored as m
c     Note: rstate stored as r; nobs stored as n
c     Note: T(t) stored as tt;  P(t) stored as pt
c     Note: H(t) stored as ht;  G(t) stored as gt
c     Note: Z(t) stored as zt;  Q(t) stored as qt
c     Note: On exit st is the state. On entry st is a matrix of random numbers

c     Input variables:
      integer m, n, p, r, mn, two_m
      integer ht_type, qt_type, gt_type, tt_type, zt_type  ! matrix indicators
      integer n_t, n_h, n_z, n_q, n_g , n_p     
      real*8 tt(m,m,n_t), qt(r,r,n_q), y(p,n)       
      real*8 ht(p,n_p,n_h), zt(p,m,n_z), gt(r,m,n)
      real*8 p1(m,m), a1(m), alpha, beta, sta(mn)
   
c     Local variables:
      integer t, info, ifo, st, lwk, timet
      integer t_z, t_h, t_t, t_q, t_g 
      real*8 z_h(m,p), gqg(m,m),  gt_i(m,r), gqg_prev(m,m)
      real*8 p1_i(m,m), p1copy(m,m), diag(m,m)
      real*8 gqgt(m,m), mu(mn) , zhz(m,m), tgqgt(m,m)
      real*8 bmat(two_m, mn), lblock(m,m)       
c ----------------------      
cf2py intent(in) y
cf2py intent(in) tt
cf2py intent(in) ht
cf2py intent(in) zt
cf2py intent(in) qt
cf2py intent(in) p1
cf2py intent(in) a1
cf2py intent(in) ht_type
cf2py intent(in) qt_type
cf2py intent(in) gt_type
cf2py intent(in) tt_type
cf2py intent(in) zt_type
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n
cf2py intent(in) r
cf2py intent(in) mn
cf2py intent(in) two_m
cf2py intent(inout) ifo
cf2py intent(inout) st
cf2py intent(in) n_h
cf2py intent(in) n_q
cf2py intent(in) n_g
cf2py intent(in) n_t
cf2py intent(in) n_z
cf2py intent(in) n_p
c ----------------------
      alpha = 1.0      
      
      ! Initialise parameter for DGESVD function
      lwk = 50
c     ------------------------------------------
c     Compute: p1_i = inv(p1) => Solve p1 * p1_i  = I
      call eye(p1_i,m)  ! Initialise as identity             

c     Make a copy: set p1copy = p1
      call mcopy(p1,p1copy,m,m)         

c     Now do solve. Note: p1copy overwritten
      call dposv('u',m,m,p1copy,m,p1_i,m,info)   
      call setflag(info, ifo)  
      if(info.gt.0) print *, "Error: Failed to solve [tv_noname_simsm]"
c     ------------------------------------------
      st = 1
      do t = 1, n-1   
               
c         Time varying matrix selection: choose t th matrix or first
          t_t = timet(n_t, t)
          t_z = timet(n_z, t)
          t_h = timet(n_h, t)
          t_q = timet(n_q, t)
          t_g = timet(n_g, t)                                        
c         -----------------------------------------------           
c         Compute: z_h 
c         Note: Computed at least once. Always computed if z or h are time varying
          if((t.eq.1).or.(n_z.gt.1).or.(n_h.gt.1)) then
              call compute_zh(ht_type, ht(:,:,t_h), zt(:,:,t_z), 
     + z_h, p, m, n_p)
          endif                
c         -----------------------------------------------           
c         Compute: gt_i using singular value decomposition
c         Note: Computed at least once. Always computed if g is time varying
          if((t.eq.1.).or.(n_g.gt.1)) then
              call compute_pseudoinv(gt(:,:,t_g), gt_i, r, m, lwk)
          endif
c         -------------------------------------------------------
c         Compute: gqg(t) = inv[G(t)]'.inv[Q(t)].inv[G(t)]
c         Note: Computed at least once. Always computed if g or q are time varying
          if((t.eq.1).or.(n_g.gt.1).or.(n_q.gt.1)) then
              call compute_gqg(qt_type, gt_type, qt(:,:,t_q), gt_i,
     + gqg, m, r, ifo)         
          endif
c         ----------------------------------                
c         Compute: gqgt(t) = gqg(t) * T;    
          if((t.eq.1).or.(n_g.gt.1).or.(n_q.gt.1).or.(n_t.gt.1)) then
              if(tt_type.eq.1) then ! is an identity matrix              
                  call mcopy(gqg, gqgt, m, m)
              else ! not identity matrix
                  beta = 0.0
                  call dgemm('n','n',m,m,m, alpha, gqg, m, tt(:,:,t_t),
     + m, beta, gqgt, m)  
              endif   
          endif                
c         ----------------------------------    
c         Compute: diag = Z'.inv[H].Z + T'.inv[Q].T               
          beta = 0.0
          
c         Note: Computed at least once. Always computed if z or h are time varying
          if((t.eq.1).or.(n_z.gt.1).or.(n_h.gt.1)) then
              call compute_zhz(zt_type, z_h, zt(:,:,t_z), zhz, 
     + beta, m, p)
          endif                        
                            
          if((t.eq.1).or.(n_t.gt.1).or.(n_g.gt.1).or.(n_q.gt.1)) then
              call compute_tgqgt(tt_type, tt(:,:,t_t), gqgt, 
     + tgqgt, beta, m)                                        
          endif
          
          call mcopy(zhz, diag, m , m)     
          call mplusm(tgqgt, diag, m, m)
c         ----------------------------------    
c         Main diagonal block calcs:                   
          if(t.eq.1) then ! Compute: diag += p1_i   
              call mplusm(p1_i, diag, m, m)
          else ! t > 1 => Compute: diag += gqg(t-1)                  
              call mplusm(gqg_prev, diag, m, m) 
          endif        
c         -----------------------------------    
c         mu calcs:
c         Compute: mu = z_h(t) * y(t)  (  == z_h_y)
          beta = 0.0
          call dgemv('n',m,p,alpha,z_h,m,y(:,t),1,beta,mu(st:st+m-1),1)
          
          if(t.eq.1) then
c             Compute: mu = mu + p1_i * a1  
              beta = 1.0                        
              call dgemv('n',m,m,alpha,p1_i,m,a1,1,beta,mu(1:m),1)
          endif            
          
          st = st + m  ! Compute next start pos, i.e. st = (t-1)*m + 1           
c         ---------------------------------------------------                       
          call mcopytr(gqgt, lblock, m, m)  ! Set lblock = transpose[gqgt]      

c         Continue construction of banded system          
c         Copy column vectors from current block matrices            
          call update_bands(bmat, diag, lblock, t, m, two_m, mn)
c         -------------------------------------------------          
          gqg_prev = gqg  ! Make a copy for next time step
      enddo 
c     -----------------------------------------------------------         
      t = n
      
c     Time varying matrix selection: choose t th matrix or first          
      t_z = timet(n_z, t)
      t_h = timet(n_h, t)
      t_q = timet(n_q, t)
      t_g = timet(n_g, t)
          
      if((t.eq.1).or.(n_g.gt.1)) then                    
          call compute_pseudoinv(gt(:,:,t_g), gt_i, r, m, lwk)  
      endif
      
c     Compute: gqg = inv[G(t)]'.inv[Q(t)].inv[G(t)]
      if((t.eq.1).or.(n_g.gt.1).or.(n_q.gt.1)) then 
          call compute_gqg(qt_type, gt_type, qt(:,:,t_q), gt_i,
     + gqg, m, r, ifo)
      endif
                
c     Compute: z_h
      if((n_z.gt.1).or.(n_h.gt.1)) then
          call compute_zh(ht_type, ht(:,:,t_h), zt(:,:,t_z), z_h,
     + p, m, n_p)
      endif
            
c     Compute: diag = z_h_z 
      beta = 0.0
      call compute_zhz(zt_type, z_h, zt(:,:,t_z), diag, beta, m, p)
      
c     Compute: diag += gqg      
      call mplusm(gqg, diag, m, m)
      
c     Compute: mu = z_h(t) * y(t)  (  == z_h_y)
      beta = 0.0             
      call dgemv('n', m, p, alpha, z_h, m, y(:,t), 1,
     + beta, mu(st:st+m-1), 1)           
                          
      call finalise_bands(bmat, diag, t, m, two_m, mn) 
c     ----------------------------------------------------                         
      call sample_state(bmat, mu, sta, mn, two_m)
      
      end
      
c ---------------------------------------------------------------------

c     Time varying (parallel) version of noname smootherc     
c     WARNING 1: MEMORY REQUIREMENTS ARE MUCH LARGER - MUST STORE ALL gqg
c     AND EACH THREAD MUST HAVE A gqgt, diag, z_h, etc
      subroutine tv_noname_simsmp(sta, y, tt, ht, zt, qt, gt, 
     + p1, a1, ht_type, zt_type, qt_type, gt_type, tt_type, ifo, 
     + two_m, mn, m, n, p, r, n_t, n_h, n_z, n_q, n_g, n_p)
     
      implicit none
c     Note: Calcs altered when zt, ht, qt, tt are be identity matrices      
c     Note: nseries stored as p; nstate stored as m
c     Note: rstate stored as r; nobs stored as n
c     Note: T(t) stored as tt;  P(t) stored as pt
c     Note: H(t) stored as ht;  G(t) stored as gt
c     Note: Z(t) stored as zt;  Q(t) stored as qt
c     Note: On exit st is the state. On entry st is a matrix of random numbers

c     Input variables:
      integer m, n, p, r, mn, two_m
      integer n_t, n_h, n_z, n_q, n_g, n_p
      integer ht_type, qt_type, gt_type, tt_type, zt_type  ! matrix indicators    
      real*8 tt(m,m,n_t), qt(r,r,n_q), y(p,n)       
      real*8 ht(p,n_p,n_h), zt(p,m,n_z), gt(r,m,n_g)
      real*8 p1(m,m), a1(m), alpha, beta, sta(mn)
   
c     Local variables:
      integer t, info, ifo, st, lwk, timet
      integer t_z, t_h, t_t, t_q, t_g
      real*8 z_h(m,p), gqg(m,m,n),  gt_i(m,r)
      real*8 p1_i(m,m), p1copy(m,m), diag(m,m)
      real*8 gqgt(m,m), mu(mn), zhz(m,m), tgqgt(m,m)
      real*8 bmat(two_m, mn), lblock(m,m)
c ----------------------      
cf2py intent(in) y
cf2py intent(in) tt
cf2py intent(in) ht
cf2py intent(in) zt
cf2py intent(in) qt
cf2py intent(in) p1
cf2py intent(in) a1
cf2py intent(in) ht_type
cf2py intent(in) qt_type
cf2py intent(in) gt_type
cf2py intent(in) tt_type
cf2py intent(in) zt_type
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n
cf2py intent(in) r
cf2py intent(in) mn
cf2py intent(in) two_m
cf2py intent(inout) ifo
cf2py intent(inout) st
cf2py intent(in) n_h
cf2py intent(in) n_q
cf2py intent(in) n_g
cf2py intent(in) n_t
cf2py intent(in) n_z
cf2py intent(in) n_p
c ----------------------
      alpha = 1.0      
      
c     WARNING 2: Initialise parameter for DGESVD function. 
c     Setting incorrect value may cause issues 
      lwk = 50
c     ------------------------------------------
c$omp parallel default(shared)

c$omp sections
c$omp section
c     Compute: p1_i = inv(p1) => Solve p1 * p1_i  = I
      call eye(p1_i,m)  ! Initialise as identity             
c$omp section
c     Make a copy: set p1copy = p1
      call mcopy(p1,p1copy,m,m)         
c$omp end sections

c$omp single
c     Now do solve. Note: p1copy overwritten
      call dposv('u',m,m,p1copy,m,p1_i,m,info)   
      call setflag(info, ifo)      
      if(info.gt.0) print *, "Error: Failed to solve [tv_noname_simsmp]"
c$omp end single
c     ------------------------------------------       
c$omp do schedule(static) private(t, gt_i, t_q, t_g)
      do t = 1, n 
c         Time varying matrix selection: choose t th matrix or first      
          t_q = timet(n_q, t)
          t_g = timet(n_g, t)                                    
c         -----------------------------------------------                                           
          ! Compute: gt_i using singular value decomposition
          if((t.eq.1.).or.(n_g.gt.1)) then
              call compute_pseudoinv(gt(:,:,t_g), gt_i, r, m, lwk)
          endif
c         -----------------------------------------------                       
c         Compute: gqg(t) = inv[G(t)]'.inv[Q(t)].inv[G(t)]
          if((t.eq.1).or.(n_g.gt.1).or.(n_q.gt.1)) then
              call compute_gqg(qt_type, gt_type, qt(:,:,t_q), gt_i,
     + gqg(:,:,t), m, r, ifo)         
          endif     
c         -----------------------------------------------                       
      enddo
c$omp end do
c     -----------------------------------------      
c$omp do schedule(static) 
c$omp& private(t_t,t_z,t_h,st,beta,gqgt,z_h,diag,zhz,tgqgt,lblock)
      do t = 1, n-1    
                
          st = (t-1)*m + 1
c         ----------------------------------                          
c         Time varying matrix selection: choose t th matrix or first          
          t_t = timet(n_t, t)
          t_z = timet(n_z, t)
          t_h = timet(n_h, t)
c         ----------------------------------                                                      
          if((t.eq.1).or.(n_z.gt.1).or.(n_h.gt.1)) then
                                
c             Compute: z_h
              call compute_zh(ht_type, ht(:,:,t_h), zt(:,:,t_z),
     + z_h, p, m, n_p)
     
c             Compute: zhz     
              beta = 0.0                    
              call compute_zhz(zt_type, z_h, zt(:,:,t_z), zhz, 
     + beta, m, p)
          endif
c         ----------------------------------                
          if((t.eq.1).or.(n_g.gt.1).or.(n_q.gt.1).or.(n_t.gt.1)) then
          
c             Compute: gqgt(t) = gqg(t) * T;                    
              if(tt_type.eq.1) then ! is an identity matrix              
                  call mcopy(gqg(:,:,t), gqgt, m, m)
              else ! not identity matrix
                  beta = 0.0
                  call dgemm('n','n',m,m,m, alpha, gqg(:,:,t), m, 
     + tt(:,:,t_t), m, beta, gqgt, m)        
           endif

c             Compute: tgqgt = T'.gqgt              
              call compute_tgqgt(tt_type, tt(:,:,t_t), gqgt, 
     + tgqgt, beta, m) 
          endif   
c         ----------------------------------     
c         Compute: diag = Z'.inv[H].Z + T'.inv[Q].T
          call mcopy(zhz, diag, m , m)     
          call mplusm(tgqgt, diag, m, m)                   
c         ----------------------------------    
c         Main diagonal block calcs:                   
          if(t.eq.1) then ! Compute: diag += p1_i   
              call mplusm(p1_i, diag, m, m)
          else ! t > 1 => Compute: diag += gqg(t-1)
              call mplusm(gqg(:,:,t-1), diag, m, m) 
          endif                     
c         -----------------------------------    
c         mu calcs:
c         Compute: mu = z_h(t) * y(t)  (  == z_h_y)
          beta = 0.0
          call dgemv('n',m,p,alpha, z_h, m, y(:,t), 1,
     + beta, mu(st:st+m-1), 1)
          
          if(t.eq.1) then
c             Compute: mu = mu + p1_i * a1  
              beta = 1.0                        
              call dgemv('n',m,m,alpha,p1_i,m,a1,1,beta,mu(1:m),1)
          endif              
c         ---------------------------------------------------             
          call mcopytr(gqgt, lblock, m, m)  ! Set lblock = transpose[gqgt]      

c         Continue construction of banded system          
c         Copy column vectors from current block matrices            
          call update_bands(bmat, diag, lblock, t, m, two_m, mn)
c         -------------------------------------------------          
      enddo   
c$omp end do
c     -----------------------------------------------------------             
c$omp single    
      t = n
      st = (t-1)*m + 1      

c     Time varying matrix selection: choose t th matrix or first
      t_z = timet(n_z, t)
      t_h = timet(n_h, t)

      if((n_z.gt.1).or.(n_h.gt.1)) then

c         Compute: z_h      
          call compute_zh(ht_type, ht(:,:,t_h), zt(:,:,t_z), 
     + z_h, p, m, n_p)
               
c         Compute: z_h_z      
          beta = 0.0
          call compute_zhz(zt_type, z_h, zt(:,:,t_z), zhz, beta, m, p)
      
      endif
      
      call mcopy(zhz, diag, m , m) 
c$omp end single      
      
c$omp sections
c$omp section     
c     Compute: diag += gqg      
      call mplusm(gqg(:,:,t), diag, m, m)  
c$omp section            
c     Compute: mu = z_h(t) * y(t)  (  == z_h_y)
      beta = 0.0                    
      call dgemv('n', m, p, alpha, z_h, m, y(:,t), 1,
     + beta, mu(st:st+m-1), 1)                  
c$omp end sections

c$omp end parallel
            
      call finalise_bands(bmat, diag, t, m, two_m, mn)             
      call sample_state(bmat, mu, sta, mn, two_m)

      end      

c ----------------------------------------------------------------------

c     Procedure calculates the transpose of a banded lower triangular matrix
      subroutine transpose_banded_lower(a, at, m, n)
c     Input: a is a banded lower triangular matrix 
c     Output: at is a banded upper triangular matrix
c     Note: at is pre initialised as zeros
      implicit none
      real*8 a(m,n), at(m,n)
      integer m, n, i, num
c ----------------------      
cf2py intent(in) a
cf2py intent(inout) at
cf2py intent(in) m
cf2py intent(in) n
c ----------------------
c$omp parallel default(shared) private(i, num)
c$omp do schedule(static)     
      do i = 1, m  ! Iterate through rows of a        
          num = n - i + 1  ! i.e. n - #zeros where #zeros = i - 1          
          at(m-i+1, i:n) = a(i, 1:num)                              
      enddo
c$omp end do
c$omp end parallel      
      end
      
c ----------------------------------------------------------------------

c     Procedure to solve a lower or upper triangular system L.x = B
c     Wrapper for function dtrsm
      subroutine solve_trsm(up, lu, b, m, n, k)
      implicit none
      integer m, n, k, up
      real*8  lu(m,n), b(m,k), alpha
      
c     Note: lu(m,n) * x(n,k) = b(m,k)
c -----------------------
cf2py intent(in) l
cf2py intent(in) up
cf2py intent(in) b
cf2py intent(in) m
cf2py intent(in) n   
cf2py intent(in) k   
c -------------------
      alpha = 1.0
      if (up.eq.1) then
          call dtrsm('l','u','n','n',m, k, alpha, lu, m, b, m)
      else
          call dtrsm('l','l','n','n',m, k, alpha, lu, m, b, m)
      endif
      end
      
c ---------------------------------------------------------------------- 
     
c     Procedure to compute inv[ht] for the time varying case
c     Note: cholesky factorisation cht also stored. It is a by
c     product of solution process
c     Note: on entry cht is a copy of ht
      subroutine compute_tv_inv_ht(ht, cht, info, p, n)
      implicit none
      integer t, i, j, p, n, info
      real*8 ht(p,p,n), cht(p,p,n)
c ----------------------      
cf2py intent(inout) ht
cf2py intent(inout) cht
cf2py intent(inout) info 
cf2py intent(in) m     
cf2py intent(in) n 
c ----------------------
c$omp parallel default(shared)
c$omp do schedule(static) private(t, i, j)
      do t = 1, n
      
c         Initialise: ht(:,:,t) = I          
          call eye(ht(:,:,t), p)
      
c         Solve: ht.inv[ht] = I  (i.e. Ax = B, where A = ht, B = cht)
c         On exit: ht is replaced with inv[ht]; cht is replaced with U    
          call dposv('u', p, p, cht(:,:,t), p, ht(:,:,t), p, info)
            
          if(info.ne.0) print *, 
     + "Error: Failed to solve [compute_tv_inv_ht]"
            
c         Zero lower triangular component of matrix      
          do i = 1, p
              do j = 1, i-1
                  cht(i, j, t) = 0.0 
              enddo
          enddo            
      enddo
c$omp end do
c$omp end parallel      
      end
      
     
c ----------------------------------------------------------------------      
      
      subroutine mult_diag_diag(diag1, diag2, res, p)
      implicit none
      integer i,p 
      real*8 diag1(p), diag2(p), res(p)
      do i = 1, p
          res(i) = diag1(i) * diag2(i)
      enddo
      end subroutine mult_diag_diag
      
c ----------------------------------------------------------------------      
      
      subroutine mult_dense_diag(dense, diag, res, n, p)
c     Compute: res = dense * diag      
      implicit none
      integer i, p, n
      real*8 dense(n,p), diag(p), res(n,p)
      
      do i = 1, p
c         Compute: res(:,i) = dense(:,i)    [i.e. copy column i]
          call dcopy(p, dense(:,i), 1, res(:,i), 1)
              
c         Compute: res(:,i) = diag(i) * res(:,i) [i.e. mult column by scalar]
          call dscal(p, diag(i), res(:,i), 1)              
      enddo
      
      end subroutine mult_dense_diag                

c ----------------------------------------------------------------------      
      
      subroutine mult_diag_dense(diag, dense, res, n, p)
c     Compute: res = diag * dense
      implicit none
      integer i, p, n
      real*8 dense(p,n), diag(p), res(p,n)
          
      do i = 1, p
c         Compute: res(i,:) = dense(i,:)   [i.e. copy row i]
          call dcopy(p, dense(i,:), 1, res(i,:), 1)
              
c         Compute: res(i,:) = diag(i) * res(i,:) [i.e. mult row by scalar]
          call dscal(p, diag(i), res(i,:), 1)              
      enddo     
      end subroutine mult_diag_dense                         
    
c ----------------------------------------------------------------------      
      
      subroutine rhr_dense(rt, ht, rt_ht, rhr, p, n_rt, n_ht, n_rhr)
c     Purpose: Compute rt * ht * rt
c     where: rt and ht are dense  

      implicit none
      integer p, t, n_rt, n_ht, n_rhr, timet, t_rt, t_ht, t_rhr, n
      real*8 rt(p,p,n_rt), ht(p,p,n_ht), rhr(p,p,n_rhr)
      real*8 rt_ht(p,p)
      real*8 alpha, beta
c ----------------------
cf2py intent(in) rt
cf2py intent(in) ht
cf2py intent(inout) rt_ht
cf2py intent(inout) rhr
cf2py intent(in) p
cf2py intent(in) n_rt
cf2py intent(in) n_ht
cf2py intent(in) n_rhr
c ----------------------
      alpha = 1.0
      beta = 0.0
      
c     Note: If both are non time varying then n = 1
      n = max(n_ht, n_rt)  

c$omp parallel default(shared) private(t, t_ht, t_rt, t_rhr, rt_ht)
c$omp do schedule(static)                    
      do t = 1, n
          t_ht = timet(n_ht,t)
          t_rt = timet(n_rt,t)
          t_rhr = timet(n_rhr,t)
          
c         Compute: rt_ht = rt * ht
          call dgemm('n','n',p,p,p,alpha, rt(:,:,t_rt), p, ht(:,:,t_ht),
     + p, beta, rt_ht, p)    
          
c         Compute: rt_ht * rt'
          call dgemm('n','t',p,p,p,alpha, rt_ht, p, rt(:,:,t_rt),
     + p, beta, rhr(:,:,t_rhr), p)    
          
      enddo
c$omp end do
c$omp end parallel         
              
      end subroutine rhr_dense
c ----------------------------------------------------------------------      
 
      subroutine rhr_diag_rt_ht(rt, ht, rt_ht, rhr, p, 
     + n_rt, n_ht, n_rhr)     
c     Purpose: Compute rt * ht * rt
c     Where: rt is diag, ht is diag      
      implicit none
      integer t_ht, t_rt, t_rhr, n, timet, p, n_rt, n_ht, n_rhr, t
      real*8 rt(p,1,n_rt), ht(p,1,n_ht), rhr(p,1,n_rhr)
      real*8 rt_ht(p,1)      
c ----------------------
cf2py intent(in) rt
cf2py intent(in) ht
cf2py intent(in) rt_ht
cf2py intent(inout) rhr
cf2py intent(in) p
cf2py intent(in) n_rt
cf2py intent(in) n_ht
cf2py intent(in) n_rhr
c ----------------------       
      
c     Note: If both are non time varying then n = 1
      n = max(n_ht, n_rt)  
      
c$omp parallel default(shared) private(t, t_ht, t_rt, t_rhr, rt_ht)
c$omp do schedule(static)                    
      do t = 1, n
          t_ht = timet(n_ht,t)
          t_rt = timet(n_rt,t)
          t_rhr = timet(n_rhr,t)             
          call mult_diag_diag(rt(:,1,t_rt), ht(:,1,t_ht),
     + rt_ht(:,1), p)
          call mult_diag_diag(rt_ht(:,1), rt(:,1,t_rt),
     +  rhr(:,1,t_rhr), p)
      enddo
c$omp end do
c$omp end parallel   
      
      end subroutine rhr_diag_rt_ht
 
c ----------------------------------------------------------------------     
 
      subroutine rhr_diag_ht(rt, ht, rt_ht, rhr, p, n_rt, n_ht, n_rhr)
c     Purpose: Compute rt * ht * rt 
c     where: rt is dense, ht is diag

      implicit none
      integer p, t, n_rt, n_ht, n_rhr, timet, t_rt, t_ht, t_rhr, n
      real*8 rt(p,p,n_rt), ht(p,1,n_ht), rhr(p,p,n_rhr)
      real*8 rt_ht(p,p)
      real*8 alpha, beta
c ------------------------
cf2py intent(in) rt
cf2py intent(in) ht
cf2py intent(inout) rt_ht
cf2py intent(inout) rhr
cf2py intent(in) p
cf2py intent(in) n_rt
cf2py intent(in) n_ht
cf2py intent(in) n_rhr
c ---------------------
      alpha = 1.0
      beta = 0.0
      
c     Note: If both are non time varying then n = 1
      n = max(n_ht, n_rt)  
      
c$omp parallel default(shared) private(t, t_ht, t_rt, t_rhr, rt_ht)
c$omp do schedule(static)              
      do t = 1, n
          t_ht = timet(n_ht,t)
          t_rt = timet(n_rt,t)
          t_rhr = timet(n_rhr,t)
                                      
c         1. Compute: rt_ht = rt * ht 
          call mult_dense_diag(rt(:,:,t_rt), ht(:,1,t_ht), rt_ht, p, p)
                                            
c         2. Compute: rt_ht * rt.T
          call dgemm('n','t',p,p,p,alpha, rt_ht, p, rt(:,:,t_rt),
     + p, beta, rhr(:,:,t_rhr), p)    
          
      enddo
c$omp end do
c$omp end parallel   
              
      end subroutine rhr_diag_ht
      
c ----------------------------------------------------------------------      

      subroutine rhr_diag_rt(rt, ht, rt_ht, rhr, p, n_rt, n_ht, n_rhr)
c     Purpose: Compute rt * ht * rt      
c     where: ht is dense, rt is diag

      implicit none
      integer p, t, n_rt, n_ht, n_rhr, timet, t_rt, t_ht, t_rhr, n
      real*8 rt(p,n_rt), ht(p,p,n_ht), rhr(p,p,n_rhr)
      real*8 rt_ht(p,p)
      real*8 alpha, beta
c ----------------------
cf2py intent(in) rt
cf2py intent(in) ht
cf2py intent(inout) rhr
cf2py intent(in) p
cf2py intent(in) n_rt
cf2py intent(in) n_ht
cf2py intent(in) n_rhr
c ----------------------
      alpha = 1.0
      beta = 0.0
      
c     Note: If both are non time varying then n = 1
      n = max(n_ht, n_rt)  
      
c$omp parallel default(shared) private(t, t_ht, t_rt, t_rhr, rt_ht)
c$omp do schedule(static)              
      do t = 1, n
          t_ht = timet(n_ht,t)
          t_rt = timet(n_rt,t)
          t_rhr = timet(n_rhr,t)
             
c         1. Compute: rt_ht = rt * ht             
          call mult_diag_dense(rt(:,t_rt), ht(:,:,t_ht), rt_ht, p, p)
                        
c         2.Compute: rhr = rt_ht * rt
          call mult_dense_diag(rt_ht, rt(:,t_rt), rhr(:,:,t_rhr), p, p)
        
      enddo
c$omp end do
c$omp end parallel         
              
      end subroutine rhr_diag_rt
      
c ----------------------------------------------------------------------
 
      subroutine rcht_dense(rt, cht, rcht, p, n_rt, n_cht, n_rcht)
c     Purpose: Compute rt * cht for all t   
c     where: rt and cht are dense   
      implicit none
      integer p, t, n_rt, n_cht, n_rcht, timet, t_rt, t_cht, t_rcht, n
      real*8 rt(p,p,n_rt), cht(p,p,n_cht), rcht(p,p,n_rcht)
      real*8 alpha, beta
c ----------------------
cf2py intent(in) rt
cf2py intent(in) cht
cf2py intent(inout) rcht
cf2py intent(in) p
cf2py intent(in) n_rt
cf2py intent(in) n_cht
cf2py intent(in) n_rcht
c ----------------------      
      alpha = 1.0
      beta = 0.0
      
      n = max(n_cht, n_rt)
      
c$omp parallel default(shared) private(t, t_cht, t_rt, t_rcht)
c$omp do schedule(static)              
      do t = 1, n
          t_cht = timet(n_cht,t)
          t_rt = timet(n_rt,t)
          t_rcht = timet(n_rcht,t)
          
c         Compute: rcht = rt * cht 
          call dgemm('n','n',p, p, p,alpha, rt(:,:,t_rt), p, 
     + cht(:,:,t_cht), p, beta, rcht(:,:,t_rcht), p)                    
       
      enddo
c$omp end do
c$omp end parallel   
    
      end subroutine rcht_dense
c ----------------------------------------------------------------------      

      subroutine rcht_diag_rt(rt, cht, rcht, p, n_rt, n_cht, n_rcht)
c     Purpose: Compute rt * cht for all t   
c     where: rt is diag and cht is dense   
      implicit none
      integer p, t, n_rt, n_cht, n_rcht, timet, t_rt, t_cht, t_rcht, n
      real*8 rt(p,1,n_rt), cht(p,p,n_cht), rcht(p,p,n_rcht)
      real*8 alpha, beta
c ----------------------
cf2py intent(in) rt
cf2py intent(in) cht
cf2py intent(inout) rcht
cf2py intent(in) p
cf2py intent(in) n_rt
cf2py intent(in) n_cht
cf2py intent(in) n_rcht
c ----------------------      
      alpha = 1.0
      beta = 0.0
      
      n = max(n_cht, n_rt)
      
c$omp parallel default(shared) private(t, t_cht, t_rt, t_rcht)
c$omp do schedule(static)        
      do t = 1, n
          t_cht = timet(n_cht,t)
          t_rt = timet(n_rt,t)
          t_rcht = timet(n_rcht,t)           
          call mult_diag_dense(rt(:,1,t_rt), cht(:,:,t_cht),
     + rcht(:,:,t_rcht), p, p)                               
      enddo
c$omp end do
c$omp end parallel   
    
      end subroutine rcht_diag_rt
      
c ----------------------------------------------------------------------      

      subroutine rcht_diag_cht(rt, cht, rcht, p, n_rt, n_cht, n_rcht)
c     Purpose: Compute rt * cht for all t   
c     where: rt is dense and cht is diag
      implicit none
      integer p, t, n_rt, n_cht, n_rcht, timet, t_rt, t_cht, t_rcht, n
      real*8 rt(p,p,n_rt), cht(p,n_cht), rcht(p,p,n_rcht)
      real*8 alpha, beta
c ----------------------
cf2py intent(in) rt
cf2py intent(in) cht
cf2py intent(inout) rcht
cf2py intent(in) p
cf2py intent(in) n_rt
cf2py intent(in) n_cht
cf2py intent(in) n_rcht
c ----------------------      
      alpha = 1.0
      beta = 0.0
      
      n = max(n_cht, n_rt)

c$omp parallel default(shared) private(t, t_cht, t_rt, t_rcht)
c$omp do schedule(static)      
      do t = 1, n
          t_cht = timet(n_cht,t)
          t_rt = timet(n_rt,t)
          t_rcht = timet(n_rcht,t)           
          call mult_dense_diag(rt(:,:,t_rt), cht(:,t_cht),
     + rcht(:,:,t_rcht), p, p)                                   
      enddo
c$omp end do
c$omp end parallel      
    
      end subroutine rcht_diag_cht

     
c ----------------------------------------------------------------------            

      subroutine calc_zt_s_ntv(st,zt,zts,p,m,n)
      implicit none
      integer p,m,n
      real*8 st(m,n),zt(p,m),zts(p,n)
      real*8 alpha,beta

cf2py intent(in) st
cf2py intent(in) zt
cf2py intent(inout) zts
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n


      alpha = 1.0
      beta = 0.0

      call dgemm('n','n',p,n,m,alpha,zt,p,st,m,beta,zts,p)
      end subroutine calc_zt_s_ntv
      

c ----------------------------------------------------------------------            

      subroutine calc_zt_s_tv(st,zt,zts,p,m,n,nz)
      implicit none
      integer p,m,n,nz,t_z,t,timet
      real*8 st(m,n),zt(p,m,nz),zts(p,n)
      real*8 alpha,beta

cf2py intent(in) st
cf2py intent(in) zt
cf2py intent(inout) zts
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n
cf2py intent(in) nz


      alpha = 1.0
      beta = 0.0

      do t=1,n
          t_z = timet(nz,t)
          call dgemv('n',p,m,alpha,zt(:,:,t_z),p,st(:,t),1,beta,
     + zts(:,t),1)
          
      enddo
      
      end subroutine calc_zt_s_tv


c     Fortran 77 function to check if entire column is nan
c     return index 0 - entire column not nan
c     return index 1 - partial column is nan
c     return index 2 - entire column is nan
      subroutine ck_col_nan(y,ind,p,n)
      implicit none
      !inputs
      integer p,n,ind(n),misnan
      real*8 y(p,n)

      !counters
      integer i,t,co

cf2py intent(in) y
cf2py intent(inout) ind

      !main part of procedure
      do t=1,n
          co=0
          do i=1,p
              co=co+misnan(y(i,t))
          enddo
          if (co.eq.p) then
              ind(t)=2 !all nan
          else if(co.eq.0) then
             ind(t)=0 !no nan
         else
            ind(t)=1 !partial nan
         endif
      enddo
      
      end subroutine ck_col_nan

c     Function returns 1 if a is nan, and 0 otherwise.
      integer function misnan(a)
      implicit none
      real*8 a

      if(isnan(a)) then
          misnan = 1
      else
          misnan = 0
      endif
      return
      end function misnan
