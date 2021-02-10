# algorithm to invert a matrix quickly

n=5000000;p=50
X=matrix(nrow=n,ncol=p,data=rnorm(n*p))
y=X[,3]-X[,5]+rnorm(n)
C=crossprod(X)
r=crossprod(X,y)

solveSys <- function(C, r, tol = 1e-9){
  p=ncol(C);b=rep(0,p);bOLD = solve(C,r);
  c <- diag(C);diag(C) <- 0
  
  ready=FALSE
  while(!ready){
    
    for(i in 1:p){
      b[i] <- (r[i] - crossprod(C[i, ], b))/c[i] }
    ready<-(max(abs(b-as.vector(bOLD))) < tol)
  }
  return(b)
}
rbind(solveSys(C,r),as.vector(solve(C,r)))
all.equal(solveSys(C,r, 1e-5), as.vector(solve(C,r)))
#this is consistent with our tolerance level