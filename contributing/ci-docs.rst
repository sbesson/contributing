Documentation jobs
------------------

All documentation jobs are listed under the :jenkinsview:`Docs <Docs>` view
tab of Jenkins. A :guilabel:`GitHub`
button in the left-side panel of the job window links to the code repository
the job is building from (alternatively, the console output for the build will
indicate where the changes are being fetched from).

More detail on how and where to edit OME documentation is available on the
:doc:`editing-docs` page.

.. list-table::
	:header-rows: 1

	-	* Job task
		* OMERO 5.x series

	-	* Builds the latest OMERO documentation for publishing
		* :term:`OMERO-DEV-latest-docs`

	-	* Builds the OMERO documentation for review
		* :term:`OMERO-docs`

	-	* Builds the auto-generated OMERO documentation
		* :term:`OMERO-DEV-latest-docs-autogen`

	-	* Builds the auto-generated OMERO documentation for review
		* :term:`OMERO-DEV-merge-docs-autogen`

The Bio-Formats documentation jobs are described in the :doc:`ci-bio-formats`
section.

The OME Model, OME help and OME Contributing documentation sets are
independent of the current OMERO/Bio-Formats version.

.. list-table::
	:header-rows: 1

	-	* Job task
		*

	-	* Build the latest OME Model documentation
		* :term:`MODEL-latest-docs`

	-	* Publish OME Contributing documentation
		* :term:`CONTRIBUTING-latest-docs`

	-	* Review OME Model documentation PRs
		* :term:`MODEL-merge-docs`

	-	* Review OME Contributing documentation PRs
		* :term:`CONTRIBUTING-merge-docs`

	-	* Review OME help documentation PRs
		* :term:`OME-help-staging`

	-	* Publish OME help documentation
		* :term:`OME-help-release`

Since OMERO.figure came under the management of the wider OME team, there are
also builds to manage its GitHub pages website, which operate the same way as
the help builds.

.. list-table::
	:header-rows: 1

	-	* Job task
		*

	-	* Review PRs opened against the OME Website
		* :term:`WWW-merge`

	-	* Review PRs opened against the OMERO.figure website
		* :term:`FIGURE-help-staging`

	-	* Publish the OMERO.figure website
		* :term:`FIGURE-help-staging`

	-	* Review PRs opened against the OME help website
		* :term:`OME-help-staging`

	-	* Publish the OME help website
		* :term:`OME-help-release`

	-	* Review PRs opened against the Presentations website
		* :term:`PRESENTATIONS-merge`


Configuration
^^^^^^^^^^^^^

For all jobs building documentation using Sphinx, the following environment
variables are used:

- the Sphinx building options, :envvar:`SPHINXOPTS`, is set to
  ``-Dsphinx.opts="-W"``

- the release number of the documentation is set by :envvar:`OMERO_RELEASE`,
  :envvar:`BF_RELEASE` or by the relevant POM

- the source code links use :envvar:`SOURCE_USER` and :envvar:`SOURCE_BRANCH`

- for the Bio-Formats and OMERO sets of documentation, the name of the
  Jenkins job is set by :envvar:`JENKINS_JOB`.

Note that the https://github.com/openmicroscopy/sphinx_theme repository is no
longer used, this hosted the theme to match the old plone website.

OMERO 5.x series
^^^^^^^^^^^^^^^^

The branch for the 5.x series of the OMERO documentation is develop.

.. glossary::

	:jenkinsjob:`OMERO-DEV-latest-docs`

		This job is used to review the PRs opened against the develop branch
		of the OMERO 5.x documentation

		#. |merge|
		#. |sphinxbuild|
		#. |linkcheck|

	:mergecijob:`OMERO-docs`

		This job is used to review the PRs opened against the develop branch
		of the OMERO 5.x documentation

		#. |merge|
		#. Pushes the branch to :omedoc_scc_branch:`merge_ci`
		#. |sphinxbuild|
		#. |linkcheck|

	:jenkinsjob:`OMERO-DEV-latest-docs-autogen`

		This job is used to build the latest auto-generated pages for the
		develop branch of the OMERO documentation

		#. Checks out the develop branch of ome-documentation.git_
		#. Downloads the latest OMERO.server and OMERO.clients
		#. Runs the :file:`omero/autogen_docs` autogeneration script
		#. Pushes the auto-generated changes to
		   :omedoc_scc_branch:`develop/latest/autogen`

	:jenkinsjob:`OMERO-DEV-merge-docs-autogen`

		This job is used to review the component auto-generation for the
		develop branch of the OMERO documentation

		#. Checks out :omedoc_scc_branch:`merge_ci`
		#. Downloads the merge OMERO.server and OMERO.clients
		#. Runs the :file:`omero/autogen_docs` autogeneration script
		#. Pushes the auto-generated changes to
		   :omedoc_scc_branch:`develop/merge/autogen`

OME Model and OME Contributing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The OME Contributing documentation is located in the ome-documentation
repository and is built from the develop branch. The Model documentation is
located in the ome-model repository and is built from the master branch.

.. glossary::

	:jenkinsjob:`MODEL-merge-docs`

		This job is used to review the PRs opened against the master branch
		of the OME Model documentation

		#. |merge|
		#. |sphinxbuild|
		#. |linkcheck|

	:jenkinsjob:`CONTRIBUTING-merge-docs`

		This job is used to review the PRs opened against the develop branch
		of the OME Contributing documentation

		#. |merge|
		#. |sphinxbuild|
		#. |linkcheck|

	:jenkinsjob:`MODEL-latest-docs`

		This job is used to build the master branch of the OME Model
		documentation and publish the official documentation

		#. |sphinxbuild|
		#. |linkcheck|

	:jenkinsjob:`CONTRIBUTING-latest-docs`

		This job is used to build the develop branch of the OME Contributing
		documentation and publish the official documentation

		#. |sphinxbuild|
		#. |linkcheck|

Jekyll websites
^^^^^^^^^^^^^^^

The following set of jobs is used to review or publish the content of the
:doc:`OME Jekyll websites <jekyll>`.

.. glossary::

	:jenkinsjob:`WWW-merge`

		This job is used to review the PRs opened against the master branch of
		https://github.com/openmicroscopy/www.openmicroscopy.org

		#. |merge| and pushes the branch to https://github.com/snoopycrimecop/www.openmicroscopy.org/tree/gh-pages
		#. The GitHub Pages service deploys the staging website content under https://snoopycrimecop.github.io/www.openmicroscopy.org/

	:jenkinsjob:`OME-help-staging`

		This job is used to review the PRs opened against the master branch
		of https://github.com/openmicroscopy/ome-help

		#. |merge| (and also incorporates :omehelp_scc_branch:`cname_staging`
		   to allow	 deployment to a non-GitHub URL) then pushes the resulting
		   branch to :omehelp_scc_branch:`gh-pages`
		#. The GitHub Pages service updates the content of
		   https://help.staging.openmicroscopy.org

	:jenkinsjob:`OME-help-release`

		This job is used to deploy the OME help documentation

		#. Opens a Pull Request from
		   https://github.com/openmicroscopy/ome-help/tree/master
		   to https://github.com/openmicroscopy/ome-help/tree/gh-pages. If
		   this PR is merged, the GitHub Pages service updates the content of
		   https://help.openmicroscopy.org
		#. If the build is promoted,
			#. rysnc the content of :file:`/ome/data_repo/public/help-staging`
			   to :file:`/ome/data_repo/public/help`

	:jenkinsjob:`FIGURE-help-staging`

		This job is used to review the PRs opened against the gh-pages-staging
		branch of https://github.com/ome/omero-figure.

		#. |merge| (and also incorporates :figure_scc_branch:`cname_staging` to
		   allow  deployment to a non-GitHub URL) then pushes the resulting
		   branch to :figure_scc_branch:`gh-pages`
		#. The GitHub Pages service updates the content of
		   https://figure.staging.openmicroscopy.org

	:jenkinsjob:`FIGURE-help-release`

		This job is used to deploy the Figure gh-pages website

		#. Opens a Pull Request from
		   https://github.com/ome/omero-figure/tree/gh-pages-staging
		   to https://github.com/ome/omero-figure/tree/gh-pages. If
		   this PR is merged, the GitHub Pages service updates the content of
		   https://figure.openmicroscopy.org

	:jenkinsjob:`PRESENTATIONS-merge`

		This job is used to review the PRs opened against the master branch of
		https://github.com/ome/presentations

		#. |merge| and pushes the branch to https://github.com/snoopycrimecop/presentations
		#. The GitHub Pages service deploys the staging website content under https://snoopycrimecop.github.io/presentations/

