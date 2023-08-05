/////////////////////////////////////////////////////////////////////////////
// Name:        dir.cpp
// Author:      Laurent Pugin
// Created:     2016
// Copyright (c) Authors and others. All rights reserved.
/////////////////////////////////////////////////////////////////////////////

#include "dir.h"

//----------------------------------------------------------------------------

#include <assert.h>

//----------------------------------------------------------------------------

#include "editorial.h"
#include "functorparams.h"
#include "text.h"
#include "verticalaligner.h"
#include "vrv.h"

namespace vrv {

//----------------------------------------------------------------------------
// Dir
//----------------------------------------------------------------------------

static const ClassRegistrar<Dir> s_factory("dir", DIR);

Dir::Dir()
    : ControlElement(DIR, "dir-")
    , TextListInterface()
    , TextDirInterface()
    , TimeSpanningInterface()
    , AttExtender()
    , AttLang()
    , AttLineRendBase()
    , AttVerticalGroup()
{
    RegisterInterface(TextDirInterface::GetAttClasses(), TextDirInterface::IsInterface());
    RegisterInterface(TimeSpanningInterface::GetAttClasses(), TimeSpanningInterface::IsInterface());
    RegisterAttClass(ATT_LANG);
    RegisterAttClass(ATT_EXTENDER);
    RegisterAttClass(ATT_LINERENDBASE);
    RegisterAttClass(ATT_VERTICALGROUP);

    Reset();
}

Dir::~Dir() {}

void Dir::Reset()
{
    ControlElement::Reset();
    TextDirInterface::Reset();
    TimeSpanningInterface::Reset();
    ResetExtender();
    ResetLang();
    ResetLineRendBase();
    ResetVerticalGroup();
}

bool Dir::IsSupportedChild(Object *child)
{
    if (child->Is({ LB, REND, TEXT })) {
        assert(dynamic_cast<TextElement *>(child));
    }
    else if (child->IsEditorialElement()) {
        assert(dynamic_cast<EditorialElement *>(child));
    }
    else {
        return false;
    }
    return true;
}

bool Dir::AreChildrenAlignedTo(data_HORIZONTALALIGNMENT alignment) const
{
    const ArrayOfObjects *children = GetChildren();
    bool hasHalign = std::any_of(children->begin(), children->end(), [&alignment](Object *child) {
        AttHorizontalAlign *hAlign = dynamic_cast<AttHorizontalAlign *>(child);
        return (hAlign && (hAlign->GetHalign() == alignment));
    });
    return hasHalign;
}

//----------------------------------------------------------------------------
// Dir functor methods
//----------------------------------------------------------------------------

int Dir::PrepareFloatingGrps(FunctorParams *)
{
    if (this->HasVgrp()) {
        this->SetDrawingGrpId(-this->GetVgrp());
    }

    return FUNCTOR_CONTINUE;
}

} // namespace vrv
