#ifndef CATTools_CatAnalyzer_KinematicSolvers_H
#define CATTools_CatAnalyzer_KinematicSolvers_H

#include "Math/LorentzVector.h"
#include <string>
#include <memory>
#include "TH1.h"

class TtFullLepKinSolver;

namespace cat {

typedef ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<double> > LV;

class KinematicSolver
{
public:
  virtual ~KinematicSolver() {};
  virtual void solve(const LV input[]) = 0;
  virtual std::string algoName() = 0;

  double quality() const { return quality_; };
  const LV& l1() const { return l1_; };
  const LV& l2() const { return l2_; };
  const LV& j1() const { return j1_; };
  const LV& j2() const { return j2_; };
  const LV& nu1() const { return nu1_; };
  const LV& nu2() const { return nu2_; };
  double aux(size_t i) const { return values_.at(i); };
  const std::vector<double>& aux() const { return values_; };

protected:
  double quality_;
  LV nu1_, nu2_;
  LV l1_, l2_, j1_, j2_;
  std::vector<double> values_;
};

class TTDileptonSolver : public KinematicSolver // A dummy solver for now
{
public:
  void solve(const LV input[]) override;
  std::string algoName() override { return "DUMMY"; }
};

class MT2Solver : public KinematicSolver
{
public:
  void solve(const LV input[]) override;
  std::string algoName() override { return "MT2"; }
  double mt2();

protected:

};

class MAOSSolver : public MT2Solver
{
public:
  MAOSSolver(): MT2Solver() {};
  std::string algoName() override { return "MAOS"; }
  void solve(const LV input[]) override;
};

class CMSKinSolver : public KinematicSolver
{
public:
  CMSKinSolver();
  std::string algoName() override { return "CMSKIN"; }
  void solve(const LV input[]) override;

protected:
  std::unique_ptr<TtFullLepKinSolver> solver_;
};

class DESYMassLoopSolver : public KinematicSolver
{
public:
  void solve(const LV input[]) override;
  std::string algoName() override { return "DESYMassLoop"; }
};

class DESYSmearedSolver : public KinematicSolver
{
public:
  DESYSmearedSolver();
  void solve(const LV input[]) override;
  std::string algoName() override { return "DESYSmeared"; }

protected:
  LV getSmearedLV(const LV& v, const double fE, const double dRot);

  std::unique_ptr<TH1> h_jetEres_, h_jetAres_;
  std::unique_ptr<TH1> h_lepEres_, h_lepAres_;
  std::unique_ptr<TH1> h_wmass_;
  std::unique_ptr<TH1> h_mbl_w_;
};

// Neutrino weighting method (from thesis by Temple)
class NuWeightSolver : public KinematicSolver
{
public:
  void solve(const LV input[]) override;
  std::string algoName() override { return "NuWeight"; }
};

}

#endif

