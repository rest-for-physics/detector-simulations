#include "TRestRun.h"

Int_t GetQE(string inputFile) {
    TRestRun* run = new TRestRun(inputFile);
    TRestAnalysisTree* aTree = run->GetAnalysisTree();

    TH1D* edepHist = new TH1D("edepHist", "Energy deposited in detector", 100, 0, 10);
    TH1D* primaryHist = new TH1D("primaryHist", "Energy of generated primary", 100, 0, 10);

    for (int n = 0; n < run->GetEntries(); n++) {
        run->GetEntry(n);

        Double_t eDep = aTree->GetObservableValue<Double_t>("g4Ana_totalEdep");
        Double_t ePrimary = aTree->GetObservableValue<Double_t>("g4Ana_energyPrimary");

        if (eDep > 0) edepHist->Fill(eDep);
        primaryHist->Fill(ePrimary);
    }



    FILE* f = fopen("output.txt", "wt");
    for (int n = 0; n < edepHist->GetNbinsX(); n++) {
        Double_t edepCounts = edepHist->GetBinContent(n + 1);
        Double_t primaryCounts = primaryHist->GetBinContent(n + 1);

        Double_t eff = edepCounts / primaryCounts;
        Double_t err = TMath::Sqrt(edepCounts) / primaryCounts;
        fprintf(f, "%4.2f\t%5.0lf\t%5.0lf\t%4.4lf\t%4.4lf\n", edepHist->GetBinCenter(n + 1), edepCounts,
                primaryCounts, eff, err);
    }
    fclose(f);


    // Plot
    
    TCanvas *c1 = new TCanvas("c1","response matrix",800,800);
    TH2D *matrix_hist = new TH2D("matrix hist","response matrix",20,0,10,20,0,10);
    matrix_hist->GetXaxis()->SetTitle("deposited Energy [keV]");
    matrix_hist->GetYaxis()->SetTitle("primary Energy [keV]");
    gPad->SetLogz();
    //gPad->SetTheta(90);
    //gPad->SetPhi(0);
    //gPad->SetLeftMargin(0.15);
    //gPad->SetBottomMargin(0.15);


    for (int n = 0; n< run->GetEntries(); n++) {
	    run->GetEntry(n);

	    Double_t eDep = aTree->GetObservableValue<Double_t>("g4Ana_totalEdep");
	    Double_t ePrimary = aTree->GetObservableValue<Double_t>("g4Ana_energyPrimary");

	    if (eDep > 0) matrix_hist->Fill(eDep,ePrimary);
    }

    matrix_hist->Draw("SURF1");


    return 0;
}

