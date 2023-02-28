import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns    # pip install seaborn if you dont have it
import matplotlib.animation as animation


def PhaseMeshErrorPlot(phase,show=True):
    fig,axs = plt.subplots(3,1)
    axs[0].set_ylabel("Estimated Error")
    axs[1].set_ylabel("Error Distribution")
    axs[2].set_ylabel("Error Distribution Integral")

    axs[0].set_yscale("log")
    axs[2].set_xlabel("t (0-1)")
    
    axs[0].grid(True)
    axs[1].grid(True)
    axs[2].grid(True)
    
    Miters = phase.getMeshIters()
    
    cols=sns.color_palette("plasma",len(Miters))
    
    tol = phase.MeshTol
    axs[0].plot([0,1],[tol, tol],color='k',linestyle='dashed',label='tol={0:.2e}'.format(tol))
    
    for i,miter in enumerate(Miters):
        axs[0].plot(miter.times,miter.error,color=cols[i],label="Iter: {}".format(i))
        
        hs = np.array(miter.times[1:]-miter.times[0:-1])
        scale =  sum( np.array(miter.distribution[0:-1])*hs)
        
        axs[1].plot(miter.times,miter.distribution/scale,color=cols[i])
        axs[2].plot(miter.times,miter.distintegral,color=cols[i])
        
    

    axs[0].legend()
    
    if(show):plt.show()
    
def OCPMeshErrorPlot(ocp,show=True):
    
    for phase in ocp.Phases:
        PhaseMeshErrorPlot(phase,show=False)
        
    if(show):plt.show()