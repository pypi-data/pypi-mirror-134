/////////////////////////////////////////////////////////////////////////////
// Name:        tabdursym.h
// Author:      Laurent Pugin
// Created:     2019
// Copyright (c) Authors and others. All rights reserved.
/////////////////////////////////////////////////////////////////////////////

#ifndef __VRV_TABDURSYM_H__
#define __VRV_TABDURSYM_H__

#include "atts_shared.h"
#include "layerelement.h"

namespace vrv {

//----------------------------------------------------------------------------
// TabDurSym
//----------------------------------------------------------------------------

/**
 * This class models the MEI <tabDurSym> element.
 */
class TabDurSym : public LayerElement, public AttNNumberLike {
public:
    /**
     * @name Constructors, destructors, and other standard methods
     * Reset method reset all attribute classes
     */
    ///@{
    TabDurSym();
    virtual ~TabDurSym();
    void Reset() override;
    std::string GetClassName() const override { return "TabDurSym"; }
    ///@}

    /** Override the method since alignment is required */
    bool HasToBeAligned() const override { return true; }

    /**
     * Add an element to a element.
     */
    bool IsSupportedChild(Object *object) override;

    //----------//
    // Functors //
    //----------//

protected:
    //
private:
    //
public:
    //
private:
    //
};

} // namespace vrv

#endif
